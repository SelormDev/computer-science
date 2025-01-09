;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Create your own image|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

(above (rectangle 150 30 "solid" "red")
       (overlay (star 15 "solid" "black")
                (rectangle 150 30 "solid" "yellow"))
       (rectangle 150 30 "solid" "green"))
(text "GHANA" 40 "brown")