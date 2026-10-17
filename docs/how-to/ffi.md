# Call C functions from Gofra

This guide shows how to call functions from a C library in Gofra.

For background on FFI, see [Wikipedia](https://en.wikipedia.org/wiki/Foreign_function_interface).
For the `extern` attribute, see [Reference: attributes](../reference/attributes.md#extern).

## Declare the external function

Mark the function with `extern` and give it a Gofra type contract:

```gofra
extern func int puts[*char[] s]
```

This matches the C declaration:

```c
int puts(const char *s);
```

`extern` functions **cannot have a body** — only a signature.

## Link the library

Tell the linker which library to link against with `-l`:

```bash
gofra build hello.gof -lraylib
```

If the library is not found by `pkg-config`, add a search directory with `-L`:

```bash
gofra build hello.gof -lraylib -L/opt/homebrew/lib --no-pkg-config
```

## Example

```gofra
extern func int puts[*char[] s]

func void main[]
    "Hello, World!" puts drop
end
```

```bash
gofra build hello.gof -lc
```

`puts` is called with a C-string; its return value is dropped.

## Limitations

### No variadic arguments

Gofra does not support calling variadic C functions (`printf`, etc.) directly.
The workaround is to write a non-variadic wrapper in C and call that:

### Calling convention

`extern` functions use the C calling convention. Gofra functions use the Gofra
calling convention. They are not interchangeable.
