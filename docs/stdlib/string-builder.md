# `std/stringbuilder`

A growable string buffer.

```gofra
#include "std/string_builder"
```

## `StringBuilder`

```gofra
struct StringBuilder
    data CStr
    len int
    cap int
end
```

| Field  | Type   | Description                 |
| ------ | ------ | --------------------------- |
| `data` | `CStr` | Buffer pointer              |
| `len`  | `int`  | Current length in bytes     |
| `cap`  | `int`  | Allocated capacity in bytes |

## Creating

### `sb_new`

```gofra
pub func *StringBuilder sb_new[]
```

Allocates a new `StringBuilder` with default capacity (`SB_DEFAULT_CAP`, 1024
bytes) and returns a pointer to it.

```gofra
var sb *StringBuilder
&sb call sb_new !<
```

/// warning | No `free`
There is no `free` for a `StringBuilder` yet. Allocations live until the
program exits.
///

/// warning | No growth
`sb_append` does not grow the buffer. Appending more than `cap` bytes
overflows. Check `len + sv.len <= cap` before appending.
///

## Appending

### `sb_append`

```gofra
pub func void sb_append[*StringBuilder sb, *string sv]
```

Appends a string to the builder. Copies `sv.len` bytes from `sv.data` into
`sb.data` at offset `sb.len`, then advances `sb.len`.

```gofra
var sb *StringBuilder
&sb call sb_new !<
sb "hello" call sb_append
```

## Converting

### `sb_to_string`

```gofra
pub func void sb_to_string[*StringBuilder sb, *string sv]
```

Points `sv.data` at the builder's buffer and sets `sv.len` to the builder's
length.

```gofra
var sb *StringBuilder
var sv string
&sb call sb_new !<
sb &sv call sb_to_string
sv call println
```

/// warning | No ownership transfer
The resulting `string` points into the builder's buffer. If the builder is
modified afterwards, the string changes too. There is no copy.
///

## Example

```gofra
var sb *StringBuilder
&sb call sb_new !<

sb "Hello, " call sb_append
sb "World!"  call sb_append

var sv string
sb &sv call sb_to_string
sv call println    // Hello, World!
```
