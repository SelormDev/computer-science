# Module 1a - Beginning Student Language

## Table of Contents

- [Module 1a - Beginning Student Language](#module-1a---beginning-student-language)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Learning Objectives](#learning-objectives)
  - [Core Concepts](#core-concepts)
    - [Expressions](#expressions)
    - [Evaluation](#evaluation)
    - [Strings and Images](#strings-and-images)
    - [Constant Definitions](#constant-definitions)
    - [Function Definitions](#function-definitions)
    - [Booleans and if Expressions](#booleans-and-if-expressions)

## Overview

This module introduces the Beginning Student Language (BSL) and the DrRacket programming environment. BSL is a simple language that is designed to help students learn the basics of programming. It is a subset of the Racket programming language.

## Learning Objectives

Learn how to:

- write expressions that operate on primitive data including numbers, strings, images and booleans.
- write constant and function definitions.
- write out the step-by-step evaluation of simple expressions including function calls.
- use the stepper to automatically step through the evaluation of an expression.
- use the Dr Racket help desk to discover new primitives.

## Core Concepts

### Expressions

An expression is a combination of operators and operands that can be evaluated to a value.
It can formed by opening a parenthesis, followed by an operator, followed by any number of operands, and closed by a parenthesis. For example, the expression `(+ 1 2)` adds the numbers 1 and 2. The expression `(+ 1 (* 2 3))` adds 1 to the product of 2 and 3.

<br>

### Evaluation

The evaluation of an expression is the process of simplifying it to a single value. For example, the expression `(+ 1 2)` evaluates to 3.

There are **two** rules for evaluation. The first rule is to reduce operands to values. The second rule is to apply the operator to the values. So, say we have `(+ 1 (* 2 3))`. This expression is a call to a premitive function so, we first evaluate all the operands to values. The operands are `1` and `(* 2 3)`. The first operand is already a value so we move on to the second operand. The second operand is a call to a primitive function so we evaluate it. The operands of the second operand are `2` and `3`. These are already values so we apply the operator to the values. Which means, multiply `2` and `3` to get `6`. Now we have the values `1` and `6`. We apply the operator + to these values to get `7`. So, the expression `(+ 1 (* 2 3))` evaluates to `7`.

```racket
(+ 1 (* 2 3))
(+ 1 6)

7
```

<br>

### Strings and Images

In this section, I learned about the string and image primitives values. We can create a string by enclosing it in double quotes. Eg. "SelormDev". I also learned a couple of primitives that operate on strings. Examples are the `string-length` and `string-append` functions. The `string-length` function returns the length of a string and the `string-append` function concatenates two strings. There's also `substring` which sorts of slices part of a string with zero based indexing.

```racket
(string-length "SelormDev")
(string-append "Selorm" "Dev")
(substring "SelormDev" 0 6)
```

I also learned about the `rectangle` and `circle` functions that create images. The `rectangle` function takes in the width and height of the rectangle and the `circle` function takes in the radius of the circle. I also learned about the `overlay` function that overlays two images on top of each other.

```racket
(rectangle 100 100 "solid" "blue")
(circle 50 "solid" "red")
(overlay (rectangle 100 100 "solid" "blue") (circle 50 "solid" "red"))
```

<br>

### Constant Definitions

A constant definition basicaly is storing a value in a constant variable. The syntax is `(define constant-name value)`. For example, `(define pi 3.14)` defines a constant `pi` with the value `3.14`. We can then use the constant in expressions. For example, `(* pi 2)` evaluates to `6.28`.

```racket
(define pi 3.14)
(* pi 2)
```

<br>

### Function Definitions

A function definition is a way to define a function that can be called later. The syntax is `(define (function-name parameter-list) body)`. For example, `(define (square x) (* x x))` defines a function `square` that takes in a parameter `x` and returns the square of `x`. We can then call the function by passing in a value. For example, `(square 5)` evaluates to `25`.

```racket
(define (square x) (* x x))
(square 5)
```

<br>

### Booleans and if Expressions
