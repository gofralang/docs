# Preprocessor

The preprocessor is a compilation stage that operates on **lexer tokens**,
before the parser. It resolves `#`-directives and macro references.

All preprocessor directives begin with `#`.

## `#include`

`#include` inserts the contents of another file at the point of the directive.

```gofra
#include "sum.gof"

func void main[]
    2 2 sum    // `sum` is defined in sum.gof
end
```

Inclusion is **recursive**: definitions from the included file are available at
the include site, and the included file may itself `#include` other files.

### Module include

Including a **directory** includes the file with the same name inside it:

```gofra
#include "dir"    // includes `dir/dir.gof`
```

This simplifies library layout: a library `foo` is a directory `foo/` with
`foo/foo.gof` as its entry point.

/// note | Include-once
Each file is included at most once per compilation, even if it is
`#include`d from multiple places.
///

### Search strategy

When resolving `#include`, Gofra searches in this order:

1. The directory of the **including** file.
2. The directory of the **main** file.
3. Include search directories (`-isd` / `--include-search-dir`).

## `#define` and `#undef`

`#define` creates a macro. `#undef` removes it.

```gofra
#define MACRO 2
```

The macro can be used anywhere in the code after its definition:

```gofra
MACRO MACRO +    // 2 2 + = 4
```

### From the command line

Macros can be defined from the CLI with `-D`:

```bash
gofra build -Ddebug=1 main.gof
```

This is useful for debug flags and feature toggles.

## `#ifdef`, `#ifndef`, `#endif`

Conditional compilation based on macro definition:

```gofra
#ifdef DEBUG
    // compiled only if DEBUG is defined
#endif

#ifndef DEBUG
    // compiled only if DEBUG is not defined
#endif
```

## Built-in macros

Gofra defines two macros for the target:

| Macro                   | Example                             | Meaning                 |
| ----------------------- | ----------------------------------- | ----------------------- |
| `OS_{NAME}`             | `OS_LINUX`, `OS_DARWIN`             | Target operating system |
| `ARCH_{NAME}`           | `ARCH_AMD64`, `ARCH_AARCH64`        | Target architecture     |
| `IS_{ENDIANNES}_ENDIAN` | `IS_LITTLE_ENDIAN`, `IS_BIG_ENDIAN` | ...                     |

For example, compiling for Darwin on ARM64 defines `OS_DARWIN` and
`ARCH_AARCH64`.
