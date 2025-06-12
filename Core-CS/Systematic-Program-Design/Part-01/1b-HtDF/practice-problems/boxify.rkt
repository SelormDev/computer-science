#lang htdp/bsl

(require 2htdp/image)

; PROBLEM:

; Use the How to Design Functions (HtDF) recipe to design a function that consumes an image, 
; and appears to put a box around it. Note that you can do this by creating an "outline" 
; rectangle that is bigger than the image, and then using overlay to put it on top of the image. 
; For example:

; (boxify (ellipse 60 30 "solid" "red")) should produce .

; Remember, when we say DESIGN, we mean follow the recipe.

; Leave behind commented out versions of the stub and template.

; Solution

;Image -> Image
;Add box around a given image

;(check-expect (boxify (ellipse 60 30 "solid" "red")) .) 

;(define (boxify image) .)    ;stub

;(define (boxify image)
;  (... image))

(define (boxify image)
  (overlay (rectangle (image-width image) (image-height image) "outline" "black") image))

(boxify (ellipse 30 30 "solid" "red"))