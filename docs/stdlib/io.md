# `std/io`

Standard input/output module.

```gofra
#include "std/io"
```

## File descriptors

| Constant  | Description     |
| --------- | --------------- |
| `STD_IN`  | Standard input  |
| `STD_OUT` | Standard output |
| `STD_ERR` | Standard error  |

## Output

### `print`

```gofra
pub func void print[*string sv]
```

Prints a string to `STD_OUT`.

```gofra
"hello" call print
```

### `println`

```gofra
pub func void println[*string sv]
```

Prints a string to `STD_OUT` followed by a newline.

```gofra
"hello" call println
```

### `eprint`

```gofra
pub func void eprint[*string sv]
```

Prints a string to `STD_ERR`.

### `eprint_fatal`

```gofra
pub no_return func void eprint_fatal[*string sv]
```

Prints `"FATAL: "` and the string to `STD_ERR`, then aborts execution. Does not
return.

### `print_int`

```gofra
pub func void print_int[int number]
```

Prints an integer to `STD_OUT`.

### `print_int64_fd`

```gofra
pub func void print_int64_fd[int fd, int num]
```

Prints an integer to the given file descriptor. Does not emit a newline.

### `print_int64_hex`

```gofra
pub func void print_int64_hex[int num]
```

Prints an integer as hexadecimal (`0x...`) to `STD_OUT`.

### `print_int64_hex_fd`

```gofra
pub func void print_int64_hex_fd[
    int fd,
    int num,
    bool show_hex_prefix,
    bool as_uppercase
]
```

Prints an integer as hexadecimal to the given file descriptor.

### `print_ptr`

```gofra
pub func void print_ptr[*void p]
```

Prints a pointer as a hexadecimal address.

## Input

### `input`

```gofra
pub func void input[CStr ptr, int len]
```

Reads a string from `STD_IN` into `ptr` up to `len` bytes. Exhausts the
remaining input buffer afterwards.

## Files

### `open_file_fd_ro`

```gofra
pub func int open_file_fd_ro[*string sv]
```

Opens a file in read-only mode. Returns a file descriptor.

### `read_file_sv`

```gofra
pub func bool read_file_sv[int fd, *string sv]
```

Reads up to `sv.len` bytes from `fd` into `sv.data`. Returns `false` on error.
