#lang racket/base

(require racket/contract
         racket/math)

(provide
 drude-epsilon
 constant-epsilon
 rayleigh-polarizability
 rayleigh-cross-sections
 simulate-sphere-response
 material-parameters
 get-drude-params
 material-list)

;; ============================================================
;; [MATERIAL DATABASE] Drude parameters for Au, Ag, Al
;; ============================================================
;; Format: (material-name omega-p gamma eps-inf)
;; omega-p: plasma frequency (eV)
;; gamma: damping rate (eV)
;; eps-inf: high-frequency permittivity (dimensionless)

(define material-parameters
  (list
    (list "Au"
          3.106    ; omega_p (eV)
          0.0132   ; gamma (eV)
          8.90)    ; eps_inf
    (list "Ag"
          3.810    ; omega_p (eV)
          0.0048   ; gamma (eV)
          3.91)    ; eps_inf
    (list "Al"
          14.83    ; omega_p (eV)
          0.098    ; gamma (eV)
          1.24)))  ; eps_inf

(define (get-drude-params material)
  "Return (list omega_p gamma eps_inf) for given material."
  (assoc material material-parameters))

(define (material-list)
  "Return list of available material names."
  (map car material-parameters))

;; ============================================================
;; [DRUDE] Complex dielectric function ε(ω)
;; ============================================================
;; ε(ω) = eps_inf - (omega_p² / (ω(ω + iγ)))
;;
;; Input: wavelength_nm (normal), material name
;; Output: (real_part, imag_part)

(define (wavelength-to-energy wl_nm)
  "Convert wavelength (nm) to photon energy (eV).
   E = hc/λ where hc = 1240 eV·nm"
  (/ 1240.0 wl_nm))

(define (drude-epsilon material wl_nm)
  "Compute complex permittivity via Drude model.
   Returns (values real imaginary)"
  (let* ([params (get-drude-params material)]
         [omega_p (list-ref params 1)]
         [gamma (list-ref params 2)]
         [eps_inf (list-ref params 3)]
         [omega_eV (wavelength-to-energy wl_nm)]
         [omega_sq (* omega_eV omega_eV)]
         [omega_p_sq (* omega_p omega_p)]
         [denom_sq (+ omega_sq (* gamma gamma))]
         [real_part (- eps_inf (/ (* omega_p_sq omega_eV) denom_sq))]
         [imag_part (/ (* omega_p_sq gamma) (* omega_eV denom_sq))])
    (values real_part imag_part)))

;; ============================================================
;; [CONSTANT EPSILON] For dielectric media
;; ============================================================
;; ε_d = n² (constant, non-absorbing)

(define (constant-epsilon n_squared wl_nm)
  "Return permittivity for a dielectric with refractive index n.
   Wavelength argument is ignored (constant).
   Returns: real permittivity (n²)"
  n_squared)

;; ============================================================
;; [POLARIZABILITY] Rayleigh quasi-static limit
;; ============================================================
;; α = 4πa³ (ε_p - ε_m) / (ε_p + 2ε_m)
;;
;; Input: radius_nm, eps_particle (complex), eps_medium (complex)
;; Output: (alpha_real, alpha_imag)

(define (complex-add z1 z2)
  "Add two complex numbers: (list re im)"
  (list (+ (car z1) (car z2))
        (+ (cadr z1) (cadr z2))))

(define (complex-sub z1 z2)
  "Subtract: z1 - z2"
  (list (- (car z1) (car z2))
        (- (cadr z1) (cadr z2))))

(define (complex-mul z1 z2)
  "Multiply: z1 * z2"
  (let* ([a (car z1)] [b (cadr z1)]
         [c (car z2)] [d (cadr z2)])
    (list (- (* a c) (* b d))
          (+ (* a d) (* b c)))))

(define (complex-div z1 z2)
  "Divide: z1 / z2"
  (let* ([a (car z1)] [b (cadr z1)]
         [c (car z2)] [d (cadr z2)]
         [denom (+ (* c c) (* d d))])
    (list (/ (+ (* a c) (* b d)) denom)
          (/ (- (* b c) (* a d)) denom))))

(define (complex-conj z)
  "Conjugate of z"
  (list (car z) (- (cadr z))))

(define (complex-mag-sq z)
  "Squared magnitude |z|²"
  (+ (* (car z) (car z))
     (* (cadr z) (cadr z))))

(define (rayleigh-polarizability radius_nm eps_particle eps_medium)
  "Compute Rayleigh polarizability α.
   
   α = 4πR³ (ε_p - ε_m) / (ε_p + 2ε_m)
   
   Inputs:
   - radius_nm: particle radius in nm
   - eps_particle: (list real imag) relative permittivity
   - eps_medium: (list real imag) relative permittivity medium
   
   Outputs: (values real imag)"
  (let* ([a (* 4 pi (expt radius_nm 3))]
         [eps_p eps_particle]
         [eps_m eps_medium]
         [numerator (complex-sub eps_p eps_m)]
         [two_eps_m (list (* 2 (car eps_m))
                          (* 2 (cadr eps_m)))]
         [denominator (complex-add eps_p two_eps_m)]
         [frac (complex-div numerator denominator)]
         [alpha (list (* a (car frac))
                      (* a (cadr frac)))])
    (values (car alpha) (cadr alpha))))

;; ============================================================
;; [CROSS SECTIONS] Rayleigh scattering cross-sections
;; ============================================================
;; k = 2π n_m / λ
;; C_ext = k Im(α)
;; C_sca = |k|⁴ |α|² / (6π)
;; C_abs = C_ext - C_sca
;;
;; Returns: (values c_ext c_sca c_abs)

(define (complex-magnitude z)
  "Magnitude |z| = √(re² + im²)"
  (sqrt (complex-mag-sq z)))

(define (rayleigh-cross-sections wl_nm radius_nm eps_particle eps_medium)
  "Compute extinction, scattering, absorption cross-sections.
   
   Inputs:
   - wl_nm: wavelength in nm
   - radius_nm: particle radius in nm
   - eps_particle: (list real imag)
   - eps_medium: (list real imag)
   
   Outputs: (values c_ext c_sca c_abs) all in nm²"
  (let* ([n_medium (sqrt (car eps_medium))]    ; assume non-absorbing
         [k (* 2 pi (/ n_medium wl_nm))])
    (define-values (alpha_r alpha_i)
      (rayleigh-polarizability radius_nm eps_particle eps_medium))
    (define alpha (list alpha_r alpha_i))
    (define c_ext (* k alpha_i))
    (define mag_sq (complex-mag-sq alpha))
    (define c_sca (/ (* (expt k 4) mag_sq)
                     (* 6 pi)))
    (define c_abs (- c_ext c_sca))
    (values c_ext c_sca c_abs)))

;; ============================================================
;; [HIGH-LEVEL API] Unified simulation function
;; ============================================================

(define (simulate-sphere-response
         #:material material
         #:wavelength-nm wl_nm
         #:radius-nm radius_nm
         #:medium-n n_med)
  "High-level API: compute full nanoparticle response.
   
   Returns: property list with all computed quantities"
  (define-values (eps_r eps_i)
    (drude-epsilon material wl_nm))
  (define eps_p (list eps_r eps_i))
  (define eps_m (list (constant-epsilon (* n_med n_med) wl_nm) 0))
  (define-values (alpha_r alpha_i)
    (rayleigh-polarizability radius_nm eps_p eps_m))
  (define-values (c_ext c_sca c_abs)
    (rayleigh-cross-sections wl_nm radius_nm eps_p eps_m))
  (list
   (list 'material material)
   (list 'wavelength-nm wl_nm)
   (list 'radius-nm radius_nm)
   (list 'medium-n n_med)
   (list 'epsilon-particle eps_p)
   (list 'polarizability (list alpha_r alpha_i))
   (list 'c-ext c_ext)
   (list 'c-sca c_sca)
   (list 'c-abs c_abs)))
