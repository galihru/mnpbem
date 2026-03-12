#lang info

(define collection 'multi)

(define deps '(("base" #:version "8.0")))

(define implies '())

(define blurb
  (list
   "Integrated computational package for single-nanoparticle electromagnetic response in the Rayleigh quasi-static limit."
   " Composes Drude dielectric model with Rayleigh polarizability and optical cross-section computation."))

(define primary-file #f)

(define categories '(math scientific-computing physics))

(define license 'GPL-3.0)

(define scribblings
  '(("scribblings/mnp-plasmon.scrbl"
     (multi-page)
     ("API Reference"))))

(define test-omit-paths '("tests"))
