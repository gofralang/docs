# Explanation

This section explains **how Gofra works and why** — the design decisions behind
the language and the compiler. It is not about _using_ Gofra, but about
_understanding_ it.

Use it when you want to know why something behaves the way it does, or how a
part of the toolchain fits together.

## How this section is organized

### Language design

Why Gofra is postfix, why it has no unsigned integers, why `char` is signed,
why function values are pointers and not functions, why something is not
supported yet. These pages explain the reasoning behind the language.

### Compiler internals

How the type checker works (a type-stack machine), how the optimizer decides
what to inline, how modules are compiled and linked. These pages explain the
pipeline from source to binary.
