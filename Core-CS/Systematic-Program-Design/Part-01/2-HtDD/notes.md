# How to Design Data

## cond Expressions

cond expressions are like if expressions in JavaScript. You can have nested `if`'s in a cond expression or `if` and `else`.

Here is an example of a cond expression:

```racket
(cond
  [(= x 0) "x is zero"]
  [(= x 1) "x is one"]
  [(= x 2) "x is two"]
  [else "x is something else"])
```

This will evaluate the first condition, checks if it's true, and it returns the value immediately. If not, it moves to the next condition and checks it as well. If all are false, it returns the value in the `else` clause.
