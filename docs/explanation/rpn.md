# Reverse Polish notation

Gofra uses **Reverse Polish notation** (RPN), also called **postfix notation**:
operators follow their operands. Where infix writes `2 + 2`, Gofra writes
`2 2 +`.

This page explains why Gofra is postfix and how the evaluation model works.
For the full list of operators, see [Reference: operators](../reference/operators.md).
For the tutorial introduction, see [Getting started](../tutorial/index.md).

## Why postfix

RPN has a few properties that make it a good fit for a stack-based compiled
language:

- **No precedence rules.** `2 2 + 3 *` is `(2 + 2) * 3`, unambiguously. There
  is no operator precedence table, no parentheses, no parsing ambiguity.
- **Direct stack machine.** Each operand pushes a value; each operator pops its
  operands and pushes the result. The syntax maps one-to-one onto the
  evaluation model.
- **Simple parser.** The parser does not need to build an expression tree for
  arithmetic — it emits stack operations directly.

The trade-off is readability: `2 2 +` is less familiar than `2 + 2` for
programmers coming from C-like languages. Gofra accepts this trade-off in
exchange for a simpler compiler and a uniform evaluation model.

## Why Gofra is not pure RPN

Gofra is a hybrid:

| Category     | Style   | Example        |
| ------------ | ------- | -------------- |
| Expressions  | postfix | `2 3 +`        |
| Declarations | prefix  | `var x int`    |
| Control flow | hybrid  | `x if ... end` |
| Intrinsics   | prefix  | `sizeof T`     |

Expressions are postfix because they map onto the stack machine. Declarations
are prefix because `var x int` reads better than `x int var`. Control flow
uses a postfix condition with a prefix keyword: `x if` reads as "if x, then".
Intrinsics are prefix because `sizeof T` reads as "sizeof of T".

Pure postfix would be consistent but unreadable for declarations. Gofra chooses
readability where it matters, postfix where the stack machine matters.

## Evaluation model

Gofra is a **stack machine**. Evaluation proceeds left to right:

1. A **literal** pushes its value onto the stack.
2. An **operator** pops its operands from the stack and pushes the result.
3. A **function call** pops its arguments and pushes the return value.

Consider:

```gofra
2 3 + 4 *
```

Step by step:

| Step | Token | Stack    |
| ---- | ----- | -------- |
| 1    | `2`   | `[2]`    |
| 2    | `3`   | `[2, 3]` |
| 3    | `+`   | `[5]`    |
| 4    | `4`   | `[5, 4]` |
| 5    | `*`   | `[20]`   |

The result is `20` — `(2 + 3) * 4` in infix.

## Stack effects

Every token has a **stack effect**: how many values it pops and how many it
pushes. This is documented as a mnemonic:

```
a b -> c
```

means "pops `a` and `b`, pushes `c`". For example:

| Token  | Mnemonic          | Meaning                  |
| ------ | ----------------- | ------------------------ |
| `+`    | `a b -> c`        | pops two, pushes one     |
| `drop` | `a -> _`          | pops one, pushes nothing |
| `copy` | `a -> a a`        | pops one, pushes two     |
| `!<`   | `addr val -> _ _` | pops two, pushes nothing |

See [Reference: operators](../reference/operators.md) for the full list.

## Variables and memory

Variables are accessed by **address**, not by name. `&x` pushes the address of
`x`; `?>` loads from an address; `!<` stores to an address:

```gofra
var x int
&x 10 !<    // store 10 into x
&x ?>       // load x
```

This is consistent with the stack model: everything is a value, including
addresses.

## Control flow

Control flow is also postfix. The condition is pushed **before** the keyword:

```gofra
1 1 == if
    "equal" print
end
```

`1 1 ==` pushes `true`; `if` pops it and decides whether to run the body.

## Comparison with infix

| Infix          | RPN          |
| -------------- | ------------ |
| `2 + 2`        | `2 2 +`      |
| `(2 + 3) * 4`  | `2 3 + 4 *`  |
| `f(a, b)`      | `a b f`      |
| `if (x) { y }` | `x if y end` |
