# `bool` type

A `bool` is a boolean type with two values: `true` and `false`. It is used for
conditions, logical operations, and flags.

## Size and alignment

| Type   | Size   | Alignment | Values          |
| ------ | ------ | --------- | --------------- |
| `bool` | 1 byte | 1         | `true`, `false` |

## Representation

Internally, a `bool` is an integer:

| Value   | Byte |
| ------- | ---- |
| `false` | `0`  |
| `true`  | `1`  |

/// note | "Invariant"
A well-formed `bool` is always `0` or `1`. Other byte values are not valid
`bool` values, but can appear after a [`REINTERPRET`](../typesystem/type-casting.md#reinterpret)
cast from an integer.
///

## Operators

### `lnot` (Logical NOT)

```gofra
true lnot    // false
false lnot   // true
```

### `&&` (Logical AND)

```gofra
true true &&    // true
true false &&   // false
false false &&  // false
```

### `||` (Logical OR)

```gofra
true false ||   // true
false false ||  // false
```

## Casts

### To `bool`

An integer can be cast to `bool` with [`NORMALIZE_BOOL`](../typesystem/type-casting.md#normalize_bool):
non-zero becomes `true`, zero becomes `false`.

```gofra
0 typecast bool    // false
42 typecast bool   // true
```

### From `bool`

A `bool` can be cast to an integer. The value extends to the integer type.

```gofra
true typecast i64    // 1
false typecast i64   // 0
```
