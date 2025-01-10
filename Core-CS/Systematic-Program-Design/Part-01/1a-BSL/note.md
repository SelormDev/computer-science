# Module 1a - Beginning Student Language

## Table of Contents

- [Module 1a - Beginning Student Language](#module-1a---beginning-student-language)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Learning Objectives](#learning-objectives)
  - [Core Concepts](#core-concepts)
    - [Expressions](#expressions)
    - [Evaluation](#evaluation)

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

### Evaluation

The evaluation of an expression is the process of simplifying it to a single value. For example, the expression `(+ 1 2)` evaluates to 3.

There are **two** rules for evaluation. The first rule is to reduce operands to values. The second rule is to apply the operator to the values.
