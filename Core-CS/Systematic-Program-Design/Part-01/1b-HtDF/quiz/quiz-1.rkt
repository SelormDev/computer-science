#reader(lib "htdp-beginner-reader.ss" "lang")((modname quiz-1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
; PROBLEM:
; Design a function that consumes two images and produces true if the first is larger than the second.

;Solution



;Image -> Boolean
;Check whether an image is larger than another

(define img1 (square 20 "solid" "yellow"))
(define img2 (square 30 "solid" "yellow"))
(define img3 (square 25 "solid" "yellow"))
(define img4 (square 50 "solid" "yellow"))

(check-expect (is-image-larger img1 img1) (> (image-width img1) (image-width img1)))
(check-expect (is-image-larger img1 img2) (> (image-width img1) (image-width img2)))
(check-expect (is-image-larger img1 img3) (> (image-width img1) (image-width img3)))
(check-expect (is-image-larger img1 img4) (> (image-width img1) (image-width img4)))
(check-expect (is-image-larger img2 img3) (> (image-width img2) (image-width img3)))
(check-expect (is-image-larger img2 img4) (> (image-width img2) (image-width img4)))
(check-expect (is-image-larger img3 img4) (> (image-width img3) (image-width img4)))

;(define (is-image-larger first-image second-image)   ;stub
;    true)

;(define (is-image-larger image1 image2)
;  (... image1 image2))

(define (is-image-larger image1 image2)
  (> (image-width image1) (image-width image2)))