# `std/char`

Utilities for working with the `char` type.

```gofra
#include "std/char"
```

## Predicates

### `is_digit`

```gofra
pub func bool is_digit[char c]
```

Returns `true` if `c` is an ASCII digit (`'0'`..`'9'`).

```gofra
'5' call is_digit    // true
'a' call is_digit    // false
```

/// warning | ASCII only
`is_digit` checks the ASCII range. It does not recognize Unicode digits.
///

## Conversion

### `digit_to_int`

```gofra
pub func int digit_to_int[char c]
```

Converts a digit character to its integer value.

```gofra
'5' call digit_to_int    // 5
'0' call digit_to_int    // 0
```

/// warning | No validation
`digit_to_int` does not check that `c` is a digit. Passing a non-digit
character returns a meaningless result.
///
