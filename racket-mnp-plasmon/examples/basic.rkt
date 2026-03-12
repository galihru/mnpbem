#lang racket

(require "../mnp-plasmon.rkt")

;; Gold nanoparticle, R=20nm, in water (n=1.33), λ=550nm
(define result
  (simulate-sphere-response
    #:material "Au"
    #:wavelength-nm 550
    #:radius-nm 20
    #:medium-n 1.33))

(displayln "=== Plasmonic Simulation Result ===")
(displayln (format "Material: ~a" (cadr (assoc 'material result))))
(displayln (format "Wavelength: ~a nm" (cadr (assoc 'wavelength-nm result))))
(displayln (format "Radius: ~a nm" (cadr (assoc 'radius-nm result))))
(displayln (format "Medium n: ~a" (cadr (assoc 'medium-n result))))
(newline)

(let ([eps (cadr (assoc 'epsilon-particle result))])
  (displayln (format "ε(λ) = ~a + i·~a" (car eps) (cadr eps))))

(let ([alpha (cadr (assoc 'polarizability result))])
  (displayln (format "α = ~a + i·~a nm³" (car alpha) (cadr alpha))))

(newline)
(displayln (format "Extinction cross-section: ~a nm²"
                   (cadr (assoc 'c-ext result))))
(displayln (format "Scattering cross-section: ~a nm²"
                   (cadr (assoc 'c-sca result))))
(displayln (format "Absorption cross-section: ~a nm²"
                   (cadr (assoc 'c-abs result))))
