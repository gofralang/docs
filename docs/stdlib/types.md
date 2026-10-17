# `std/types`

Type aliases and generic helpers used across the standard library.

```gofra
#include "std/types"
```

## Aliases

| Alias         | Definition | Description            |
| ------------- | ---------- | ---------------------- |
| `CStr`        | `*char[]`  | C-style string pointer |
| `Array{T, N}` | `T[N]`     | Generic array alias    |
| `Pointer{T}`  | `*T`       | Generic pointer alias  |

## `CStr`

`CStr` is a C-string pointer — a null-terminated `char` array:

```gofra
type CStr *char[]
```

Used by [`std/io`](./io.md), [`std/string`](./string.md), and FFI.

## `Array{T, N}`

A generic alias for a fixed-size array:

```gofra
type Array{T, N} T[N]

var a Array{T = int, N = 3}    // int[3]
```

## `Pointer{T}`

A generic alias for a pointer:

```gofra
type Pointer{T} *T

var p Pointer{T = int}    // *int
```
