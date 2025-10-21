#lang htdp/bsl

; (require 2htdp/image)

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

(define (fn-for-building-status status)
  (cond [(string=? "new" status) (...)]
        [(string=? "old" status) (...)]
        [(string=? "heritage" status) (...)]))


;; =================
;; Functions:

; PROBLEM B:

; The city wants to demolish all buildings classified as "old". 
; You are hired to design a function called demolish? 
; that determines whether a building should be torn down or not.