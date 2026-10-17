# `string` type

Strings in Gofra are represented as **fat pointers** — also known as
**string views** or **string slices**.

A `string` is a pair of:

- a pointer to the underlying bytes (`*char[]`),
- a length in bytes (`int`).

The data itself is not owned by the `string` value — it lives elsewhere
(typically in a read-only static data segment).

## Examples

```gofra
//"Declaration"
var s string = "Hello"

"another text" // *string

s.data   // *char[] — pointer to bytes
s.len    // 5 — byte length

// Passing around
func get_len[*string s]
    s.len
end

&s print_len // 5
"test" get_len // 4
```

## Fields

| Field   | Type      | Description                              |
| ------- | --------- | ---------------------------------------- |
| `.data` | `*char[]` | Pointer to the underlying C-string bytes |
| `.len`  | `int`     | Length in **bytes** (not characters)     |

### `.data`

Underlying pointer to the C-string (`*char[]`).

### `.len`

Size of the string in **bytes**.

## Internal representation

The `string` type is a structure available to every compiled program. It is
defined as:

```gofra
struct string
    data *char[]
    len int
end
```

## Storage

String literals are stored in the **static data segment** of the compiled
binary and must have **read-only memory protection**.

This means:

- The bytes are not copied when a `string` value is passed around.
- A `string` value does **not** own its data.
- Modifying the underlying bytes is undefined behavior.
