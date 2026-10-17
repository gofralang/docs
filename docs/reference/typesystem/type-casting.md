# Type casting (typecast)

Keyword `typecast` is used for explicit casting type `A` to type `B` (`value typecast T`)

## Example

```gofra
120 typecast i8 // i64 (int) -> i8

// Casting pointers
var x i64 = 120;
&x typecast *i8 // *i64 -> *i
?> // Resolves to i8

// Warning: useless typecast
120 typecast i64 // i64 -> i64

// Error: cannot cast type `int` to type `T1`
struct T1 ... end
120 typecast T1  // i64 -> T1
```

## Cast types

| Kind             | Description                                         |
| ---------------- | --------------------------------------------------- |
| `REINTERPRET`    | Does not modify the value — only its interpretation |
| `TRUNCATE`       | Loses information — target is smaller than source   |
| `EXTEND`         | Adds information — target is larger than source     |
| `NORMALIZE_BOOL` | Compares against zero — non-zero becomes `true`     |

## Cast rules

| From      | To        | Kind             | Notes                                                                 |
| --------- | --------- | ---------------- | --------------------------------------------------------------------- |
| `*T`      | `*U`      | `REINTERPRET`    | Any pointer to any pointer                                            |
| `integer` | `*T`      | `REINTERPRET`    | Integer size must equal pointer size (e.g. `i64` on 64-bit)           |
| `*T`      | `integer` | `REINTERPRET`    | Same constraint as above                                              |
| `bool`    | `integer` | `REINTERPRET`    | Boolean invariant, extends to integer                                 |
| `T`       | `T`       | `REINTERPRET`    | Both integer or `char`, same byte size (e.g. `i8` → `char`)           |
| `T`       | `T`       | `TRUNCATE`       | Both integer or `char`, source bigger than target (e.g. `i64` → `i8`) |
| `T`       | `T`       | `EXTEND`         | Both integer or `char`, target bigger than source (e.g. `i8` → `i64`) |
| `integer` | `bool`    | `NORMALIZE_BOOL` | Non-zero → `true`, zero → `false`                                     |

Casts not listed above are rejected at compile time.

### `REINTERPRET`

Does not modifies value, just another interpretation of bytes

- *T -> *T (any pointer to any pointer)
- integer -> *T (treating integer as pointer requires integer size to be same as target architecture pointer size, such on 64bit, integer must be `i64`, as others has invariant pointer)
- *T -> integer (same as `int -> *T`)
- bool -> integer (therefore, booleans invariants integer, it does _extends_ to integer)
- T -> T, where both are integer nor char and their byte size is same (i8 -> char)

### `TRUNCATE`

Cast with losing information

- T -> T, where both are integer nor char and source type byte size is bigger (i64 -> i8)

### `EXTEND`

Cast without losing information: add additonal bytes

- T -> T, where both are integer nor char and target type byte size is bigger (i8 -> i64)

### `NORMALIZE_BOOL`

Does compares value against zero, true on non-zero value

- integer -> bool
