#lang htdp/bsl

;PROBLEM:
;
;DESIGN function that consumes a string and determines whether its length is
;less than 5.  Follow the HtDF recipe and leave behind commented out versions 
;of the stub and template.

;; Solution:

; String -> Boolean
; Determine whether the length of a string is less than 5

; (check-expect (is-length-long "hello") (< (string-length "hello") 5))
; (check-expect (is-length-long "friend") (< (string-length "friend") 5))
; (check-expect (is-length-long "best") (< (string-length "best") 5))

; (define (is-length-long s) true)          ;stub

(define (is-length-long s)                  ;template
    (... s))