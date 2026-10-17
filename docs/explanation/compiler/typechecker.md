# Type checker

Type checking is always performed at compile time. It validates stack usage
and function calls.

This page explains how the type checker works. For the `typecast` operator, see
[Reference: type casting](../../reference/typesystem/type-casting.md)

## Type-stack machine

The type checker is a **type-stack machine**: it behaves like a stack machine,
but operates on types instead of values.

For example, the literal `2` resolves to:

```
typestack = [int]
```

Pushing `2` pushes `int` onto the type stack. Applying `+` pops two `int`s and
pushes one `int`.

## Coverage

The type checker visits **every function**, including unused ones. A function
that is never called is still checked — its body must type-check.

The exception is function **calls**: an unused function has no calls to check
against its signature.

/// note | DCE before type checking
If [DCE](./optimizations.md) is enabled, it runs **before** the type
checker. Functions removed by DCE are not type-checked.
///

## Function checking

For each function, the type checker:

1. Starts with an empty type stack.
2. Pushes parameter types as they are consumed.
3. Validates each operation against the stack.
4. Checks the return type against the function signature.

When a call is found, the type checker:

1. Pops the parameter types from the type stack.
2. Pushes the return type, unless it is `void`.
