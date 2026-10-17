# `std/string`

String conversion helpers.

```gofra
#include "std/string.gof"
```

## Types

`CStr` is a C-string pointer — an alias for `*char[]`.

## Conversions

### `string_to_cstr`

```gofra
pub func CStr string_to_cstr[*string sv]
```

Returns the underlying C-string pointer of a `string`.

```gofra
var s = "hello"
s call string_to_cstr    // *char[]
```

### `int_to_cstr`

```gofra
pub func CStr int_to_cstr[int num]
```

Converts an integer to a null-terminated C-string.

```gofra
42 call int_to_cstr    // "42"
```

/// warning | Negative numbers
Negative numbers are not supported. `int_to_cstr` returns `0` (null
pointer) for negative input.
///

/// warning | Shared buffer
The result points into a **global static buffer**. It is overwritten by the
next call to `int_to_cstr`. Copy the result if you need to keep it.
///

## Internals

The module uses two global buffers:

```gofra
var int64_to_cstr_swap_buf char[20]
var int64_to_cstr_buf      char[20]
```

`int_to_cstr` writes digits in reverse into the swap buffer, then copies them
in order into the output buffer and null-terminates.
