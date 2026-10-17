# `std/random`

Pseudo-random number generator (PRNG).

```gofra
#include "std/random"
```

/// note | Xorshift
The PRNG uses the [Xorshift](https://en.wikipedia.org/wiki/Xorshift)
algorithm. It is not cryptographically secure.
///

## State

The PRNG has a single global state:

```gofra
var std_prng_random_state int
```

Global variables are zero-initialized. To get non-deterministic output, seed
the state explicitly.

## Seeding

### `set_random_seed`

```gofra
pub func void set_random_seed[int seed]
```

Sets the PRNG state to `seed`.

```gofra
12345 call set_random_seed
```

## Generating

### `random`

```gofra
pub func int random[]
```

Advances the PRNG state and returns the next value.

```gofra
call random    // some int
```

### `random_range`

```gofra
pub func int random_range[int to]
```

Returns a value in `0..to-1`.

```gofra
10 random_range    // 0..9
```

/// warning "Not modulo-bias-free"
`random_range` uses modulo, which introduces a slight bias when `to` is
not a power of two. For most uses this is acceptable.

## Internals

### `prng_randomize_state_xorshift`

```gofra
pub func void prng_randomize_state_xorshift[]
```

Advances the PRNG state with the Xorshift step. Called by `random`.

```gofra
call prng_randomize_state_xorshift
```
