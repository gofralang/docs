# Integer types

Gofra has fixed-size **signed** integer types. All integer types are primitive:
they have a known size in bytes and a known alignment, both equal to the size.

/// note | No unsigned types
There are no unsigned integer types (`u8`, `u16`, `u32`, `u64`).
All integer types are signed.
///

## Size and alignment

| Type  | Size    | Alignment | Range                           |
| ----- | ------- | --------- | ------------------------------- |
| `i8`  | 1 byte  | 1         | −128 .. 127                     |
| `i16` | 2 bytes | 2         | −32 768 .. 32 767               |
| `i32` | 4 bytes | 4         | −2 147 483 648 .. 2 147 483 647 |
| `i64` | 8 bytes | 8         | −2^63 .. 2^63 − 1               |

## `int` alias

`int` is a language-level alias for `i64`. It is the canonical integer type used
throughout the standard library and in examples.

```gofra
var x int   // same as `var x i64`, 8 bytes
var y i64   // explicit 64-bit
var z i32   // 32-bit
var w i8    // 8-bit
```

/// note | `int` is not architecture dependant
`int` is always 64-bit on every target. It does **not** depend on the pointer
width or on the target architecture.
///

## Arithmetic

Integer types support the arithmetic operators `+`, `-`, `*`, `/`, `%`.
