# Gofra

/// warning | Beta
Gofra is in beta. The language and toolchain may change.
///

/// note | Recreational programming
Gofra is not competing with other languages. It is another incomplete
language, much like the others.
///

**A Stack-based compiled programming language.**

Gofra is a **concatenative** (stack-based) language that compiles to native
code. Programs are written in
[Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation):
operations follow their operands (`2 + 2` is `2 2 +`).

## Quick start

```gofra
#include "std"

func void main[]
    "Hello, World!" println
end
```

## Features

- _Native_ - Compiles to native machine code
- _C_-like - Close to C, but has a few more high-level abstraction (`for in`, `type generics`)
- _C FFI_ - Seamless integration with **C**-FFI libraries
- _Low-level_ - Write unsafe, low-level code with direct memory access
- _Type System_ - Validate types at compile time, has compile-time warnings (Partial generics supports, typechecker)
- _Library_ - By default has support for `math`, `random`, `network` and other libraries
- _First class functions_ - Has support, and lambda definitions (no closures/capturing yet)

## Showcase

- Pong Game (`examples/03_pong.gof`)
- Simple HTTP server (`examples/04_http_server.gof`)

## Platform support

Gofra currently supports native compilation (no cross-compilation yet). Compile on the same platform as your target.

| Platform               | Status  |
| ---------------------- | ------- |
| AArch64 macOS (Darwin) | Full    |
| x86_64 macOS (Darwin)  | Partial |
| x86_64 Linux           | Partial |
| WASM32                 | Partial |
| x86_64 Windows         | Planned |

## Install

```bash
pip install gofra
gofra --help
```

For full instructions, see [Installation](./how-to/installation.md).

## Where to go next

- **New to Gofra?** Start with the [tutorial](./tutorial/index.md).
- **Want to accomplish something?** See [how-to](./how-to/index.md).
- **Need exact syntax?** See [reference](./reference/index.md).
- **Want to understand why?** See [explanation](./explanation/index.md).
