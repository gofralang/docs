# Array types

An array is a contiguous, fixed-size block of elements of the same type. The
size is part of the type and cannot change after declaration.

## Syntax

The array type is written as the element type followed by square brackets:

```gofra
int[32]    // array of 32 integers
char[256]  // array of 256 chars
int[]      // incomplete array (see below)
```

## Layout

An array is a contiguous block of memory. The array value points to the first
element; subsequent elements follow at byte offsets scaled by the element size.

```
//  [element0][element1][element2]
//   ^
// array
```

For `int` (8 bytes), `int[3]` is laid out as:

| Index | Offset (bytes) |
| ----- | -------------- |
| `0`   | 0              |
| `1`   | 8              |
| `2`   | 16             |

/// note | Byte-scaled pointer arithmetic
Gofra pointer arithmetic is **byte-scaled**, not element-scaled. To reach
element `i` of `int[N]`, add `i 8 * ` (`i sizeof int *`) bytes — not `i`. The `[]` operator
does this scaling automatically.
///

## Initialization

Initialization depends on **storage duration**:

| Storage         | Initialization                                   |
| --------------- | ------------------------------------------------ |
| Global / static | **Zero-initialized**                             |
| Stack (local)   | **Uninitialized** — reading before writing is UB |

/// danger | "Uninitialized stack arrays"
Stack arrays are not zero-initialized. The contents are whatever was on the
stack before. Always initialize before reading.
///

### List initializer

An array can be initialized with a list of values:

```gofra
var a int[3] = [1, 2, 3]
```

The array size must match the number of values:

```gofra
var a int[3] = [1, 2, 3]    // OK
var b int[2] = [1, 2, 3]    // error: too many values
var c int[4] = [1, 2, 3]    // error: too few values
```

### Filler

To fill the remaining elements with a value, use `;` followed by the filler:

```gofra
var a int[5] = [1, 2, 3; 0]    // [1, 2, 3, 0, 0]
```

The filler applies to all elements after the explicitly listed ones.

### Manual initialization

For other types, or to set values conditionally, write to elements directly:

```gofra
var a int[3]
&a[0] 10 !<
&a[1] 20 !<
&a[2] 30 !<
```

After this, all three elements are initialized and safe to read.

## Accessing elements

The `[]` operator computes the address of the element at the given index:

```gofra
var a int[32]

a[0]    // int — first element
a[3]    // int — fourth element
```

The index can be a constant or a variable:

```gofra
var i int = 3
a[i]    // int — element at index `i`
```

### Pointer arithmetic equivalent

`a[i]` is equivalent to:

```gofra
a 8 i * +    // a + (8 * i) — for int (8 bytes)
```

## Bounds checking

Gofra performs **compile-time** bounds checking where the index is a constant:

```gofra
var a int[5]
a[5]    // compile error: index out of bounds for `int[5]`
```

/// warning | Runtime bounds are not checked
When the index is a runtime value, Gofra does **not** check bounds.
Accessing out-of-bounds memory is undefined behavior (segfault).

This can be overriden via experimental flag: `--rt-bounds-checks`/`--oob-checks`
///

## Incomplete arrays

An **incomplete** array type is written `T[]` — with no size. It cannot be used
as a variable or field type:

```gofra
var x int[]    // error: incomplete array type
```

It is used as a **function parameter type**, meaning "an array of any size":

```gofra
func void process[*int[]]
    // ...
end
```

The function accepts `*int[N]` for any `N`:

```gofra
var a int[32]
var b int[1]

&a call process    // OK
&b call process    // OK
```

/// note | No size information
An incomplete array parameter does not carry its length. If the function
needs the size, pass it as a separate parameter.
///
