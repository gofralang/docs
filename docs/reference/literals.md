# Literals

A literal is a value written directly in source code. In Gofra's postfix
syntax, a literal **pushes its value onto the stack**.

```gofra
42          // pushes 42
0x4124      // pushes 16676
-17         // pushes -17
"hello"     // pushes a string (*string)
'a'         // pushes a char
true        // pushes a bool
```

## Integer literals

Integer literals are written in decimal or hexadecimal:

```gofra
42
0
-17
0x4124
0xFF
```

Type: `int` (8 bytes, signed).

/// note | Negative literals
`-17` is a single integer literal, not the unary minus applied to `17`.
The sign is part of the literal.
///

/// note | Hexadecimal
`0x4124` is the same value as `16676` in decimal.
///

## Character literals

Character literals use single quotes:

```gofra
'a'
'Z'
'\n'
'\0'
'\x41'
```

## String literals

String literals use double quotes:

```gofra
"hello"
""
"Hello, World\n"
```

Type: `*string`. See
[`string`](./types/string.md) for details.

## Boolean literals

```gofra
true
false
```
