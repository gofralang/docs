# Module system

/// warning | Work in progress
The module system is incomplete — both the implementation and this
documentation. Use at your own risk.
///
Gofra has two ways to inject code from other files:

- `#include` — the C/C++ preprocessor way. See
  [Reference: preprocessor](../reference/preprocessor.md).
- `import` — the module system. This page.

The module system is enabled with the `FEATURE_ALLOW_MODULES`
flag in `libgofra`.

## What is a module

A module is a single `.gof` file, compiled **separately** into its own object
file. The root module is the one passed to `gofra`.

Example:

```gofra
// a.gof — root module
import b

func void main[]
    call b.hello_world
end
```

```gofra
// b.gof — dependency
#include "std"

pub func void hello_world[]
    "Hello, World!" call println
end
```

Compiling `a.gof`:

1. The compiler parses `a.gof` and finds `import b`.
2. It locates and compiles `b.gof` into `b.o`.
3. It compiles `a.gof` into `a.o`, resolving `b.hello_world` against `b.o`.
4. It links `a.o` and `b.o` into `a`.

## Import syntax

```gofra
import a                  // a.gof as `a`
import a as my_module     // a.gof as `my_module`
import "my_file.gof" as m // my_file.gof as `m`
```

## Visibility

By default, all symbols are **private**. Mark exposed symbols with `pub`:

| Visibility        | Meaning                                    |
| ----------------- | ------------------------------------------ |
| `pub`             | Available in the module and its dependants |
| private (default) | Available only within the module           |

Calling a private symbol from another module is a compile error.

## Search order

Module search follows the same rules as `#include`:

1. The directory of the current file.
2. The toolchain's working directory.
3. Include paths (`-isd` / `--include-search-dir`).

## Dependency order

Dependencies are resolved from source order. A DAG topological sort is applied
before codegen:

```
a -> b -+-> c
        |
        +-> d
```

Dependencies are compiled first, then the root module.

## Type checking and optimization

Every module is type-checked independently. Each function symbol is re-checked
on compilation.

The optimizer runs in two phases:

1. **Dependencies first**, in topological order.
2. **Root module last**, over already-optimized dependencies.

This lets the root module apply expensive, high-level optimizations over
dependencies without re-optimizing them.
