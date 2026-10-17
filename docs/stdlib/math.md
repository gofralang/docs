# `std/math`

Integer math helpers.

```gofra
#include "std/math"
```

/// note | Integer only
Gofra has no floating-point types yet. This module provides integer-only
math.
///

## Powers

### `ipow`

```gofra
pub func int ipow[int base, int exponent]
```

Integer power `base^exponent`. Negative exponents return `0`.

```gofra
2 10 ipow    // 1024
```

### `pow`

Alias for `ipow`:

```gofra
#define pow ipow
```

## Roots

### `isqrt`

```gofra
pub func int isqrt[int n]
```

Integer square root (floor), using the Babylonian method.

```gofra
16 isqrt    // 4
17 isqrt    // 4
```

### `sqrt`

Alias for `isqrt`:

```gofra
#define sqrt isqrt
```

## Absolute value

### `abs`

```gofra
pub func int abs[int x]
```

Absolute value of an integer.

```gofra
-5 abs    // 5
5 abs     // 5
```

## Min / max

### `min`

```gofra
pub func int min[int a, int b]
```

Minimum of two values.

### `max`

```gofra
pub func int max[int a, int b]
```

Maximum of two values.

## Sign

### `sign`

```gofra
pub func int sign[int x]
```

Sign of a value: `-1`, `0`, or `1`.

## Clamp

### `clamp`

```gofra
pub func int clamp[int n, int a, int b]
```

Clamps `n` to the range `[a, b]`.

```gofra
15 0 10 clamp    // 10
-5 0 10 clamp    // 0
5 0 10 clamp     // 5
```

## Factorial

### `factorial`

```gofra
pub func int factorial[int n]
```

Factorial `n!`.

```gofra
5 factorial    // 120
```

## Alignment

### `align_up`

```gofra
pub func int align_up[int size, int alignment]
```

Rounds `size` up to the next multiple of `alignment`.

```gofra
10 8 align_up    // 16
```

### `align_down`

```gofra
pub func int align_down[int size, int alignment]
```

Rounds `size` down to the previous multiple of `alignment`.

```gofra
10 8 align_down    // 8
```
