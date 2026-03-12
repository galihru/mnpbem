#lang racket/base

(require rackunit
         "../mnp-plasmon.rkt")

(test-case "Material database"
  (check-equal? (length (material-list)) 3)
  (check-true (member "Au" (material-list)))
  (check-true (member "Ag" (material-list)))
  (check-true (member "Al" (material-list)))
  (check-false (get-drude-params "Pt")))

(test-case "Drude epsilon for Au"
  (let-values ([(re im) (drude-epsilon "Au" 550)])
    (check-true (real? re))
    (check-true (real? im))
    (check-true (im . > . 0))  ; positive imaginary part
    (check-true (re . < . 0))))  ; negative real part at resonance

(test-case "Constant epsilon for water"
  (let ([eps (constant-epsilon (* 1.33 1.33) 550)])
    (check-equal? eps 1.7689)))

(test-case "Rayleigh polarizability"
  (let-values ([(alpha_r alpha_i)
                (rayleigh-polarizability 20
                                        (list -7.5 2.1)  ; Au at 550nm
                                        (list 1.769 0))])
    (check-true (real? alpha_r))
    (check-true (real? alpha_i))))

(test-case "Cross-sections are positive"
  (let-values ([(c_ext c_sca c_abs)
                (rayleigh-cross-sections 550 20
                                        (list -7.5 2.1)
                                        (list 1.769 0))])
    (check-true (c_ext . > . 0))
    (check-true (c_sca . > . 0))
    (check-true (c_abs . > . 0))
    (check-true (c_ext . > . c_sca))))  ; extinction > scattering

(test-case "High-level API returns complete result"
  (let ([result (simulate-sphere-response
                  #:material "Au"
                  #:wavelength-nm 550
                  #:radius-nm 20
                  #:medium-n 1.33)])
    (check-true (list? result))
    (check-equal? (cadr (assoc 'material result)) "Au")
    (check-equal? (cadr (assoc 'wavelength-nm result)) 550)
    (check-true (real? (cadr (assoc 'c-ext result))))))
