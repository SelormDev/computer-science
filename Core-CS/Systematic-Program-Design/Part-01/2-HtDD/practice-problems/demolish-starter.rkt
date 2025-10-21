#lang htdp/bsl

;; =================
;; Data definitions:

; PROBLEM A:

; You are assigned to develop a system that will classify 
; buildings in downtown Vancouver based on how old they are. 
; According to city guidelines, there are three different classification levels:
; new, old, and heritage.

; Design a data definition to represent these classification levels. 
; Call it BuildingStatus.

; Solution

;; BuildingStatus is one of:
;; - "new"
;; - "old"
;; - "heritage"
;; interp. classification level of a building

;; <examples are redundant for enumerations>

#;
(define (fn-for-building-status status)
  (cond [(string=? "new" status) (...)]
        [(string=? "old" status) (...)]
        [(string=? "heritage" status) (...)]))

;; Template rules used:
;;  - one of: 3 cases
;;  - atomic distinct: "new"
;;  - atomic distinct: "old"
;;  - atomic distinct: "heritage"


;; =================
;; Functions:

; PROBLEM B:

; The city wants to demolish all buildings classified as "old". 
; You are hired to design a function called demolish? 
; that determines whether a building should be torn down or not.

; Solution


;; BuildingStatus -> Boolean                           ;signature

;; Determine whether a building should be torn down    ;purpose

(check-expect (demolish "new") false)
(check-expect (demolish "old") true)
(check-expect (demolish "heritage") false)


;(define (demolish? stat) "old")                      ;stub

; Use template from BuildingStatus

(define (demolish status)
  (cond [(string=? "old" status) true]
        [else false]))
