# `char` type

A `char` is a single-byte character type.

## Size and alignment

| Type   | Size   | Alignment | Range         |
| ------ | ------ | --------- | ------------- |
| `char` | 1 byte | 1         | `−128 .. 127` |

## Relationship to `i8`

`char` and [`i8`](./integers.md) are both 1 byte, but they are **distinct
types**. Converting between them requires an explicit
[`typecast`](../typesystem/type-casting.md):

```gofra
'a' typecast i8    // 97
97 typecast char   // 'a'
```

The cast is [`REINTERPRET`](../typesystem/type-casting.md#reinterpret) — the byte is not
modified.

## Literals

Character literals use single quotes:

```gofra
// push char code on the stack
'a'
'Z'
'0'
' '
```
