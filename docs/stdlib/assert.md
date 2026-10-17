# `std/assert`

Runtime assertions.

```gofra
#include "std/assert.gof"
```

## `runtime_assert`

```gofra
pub func void runtime_assert[int a, int b, *string sv]
```

Checks that `a == b`. If not, prints `"runtime_assert: Assertion failed, "`
followed by `sv` to `STD_ERR`, then calls `abort`.

```gofra
1 1 "values must be equal" call runtime_assert    // passes
1 2 "values must be equal" call runtime_assert    // aborts
```

## `assert`

Alias for `runtime_assert`:

```gofra
#define assert runtime_assert
```

```gofra
1 1 "values must be equal" call assert
```

/// warning | Integers only
`runtime_assert` compares `int` values. It cannot compare other types
(generics are not supported yet).
///

/// warning | Aborts the process
On failure, `runtime_assert` calls `abort`. It does not throw or return.
///
