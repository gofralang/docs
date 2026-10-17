# Structures

A `struct` is a composite type with named fields of possibly different types.
Fields are laid out contiguously in memory, with padding inserted to satisfy
each field's alignment.

## Syntax

```gofra
struct <Name>
    <field> <Type>
    <field> <Type>
    ...
end
```

## Declaration

```gofra
struct Person
    age int
    name *char[]
end
```

## Field access

Fields are accessed with `.` (dot). The expression pushes the **address** of the
field, so it can be used as an lvalue for both reading and writing.

```gofra
var stepan Person

stepan.age        // int — value of `age`
&stepan.age        // *int — address of `age`

a.b.c.d // Also possible
```

## Memory layout

Fields are laid out in declaration order, with padding inserted to satisfy
each field's alignment. The total size is rounded up to the struct's alignment.

```gofra
struct BadLayout
    a char   // offset 0,  size 1
    b int    // offset 8,  size 8 (7 bytes padding before)
    c char   // offset 16, size 1
end
// sizeof = 24, align = 8
```

Layout diagram:

```
Packed (tight):
|a|    b   |c|          => 10 bytes

Aligned:
|a|...padding...|    b    |...padding...|c|   => 24 bytes
```

Padding is inserted on both sides of `b` to align the 8-byte `int` field.

## Attributes

### `packed`

Removes all padding between fields:

```gofra
struct packed Tight
    a char
    b int
    c char
end
// sizeof = 10
```

### `reorder`

Reorders fields to eliminate padding, keeping alignment:

```gofra
struct reorder Reordered
    a char
    b int
    c char
end
// Reordered to [b, a, c], sizeof = 16
```

See [`packed`](../attributes.md#packed) and [`reorder`](../attributes.md#reorder)
for details.

## Self-reference

A struct can contain a reference to itself or itself:

```gofra
struct Node
    value int
    next *Node
end
```

## Introspection

### `offset_of`

Pushes the byte offset of a field within a struct:

```gofra
offset_of <Struct> <field>
```

```gofra
struct Foo
    a int
    b int
end

offset_of Foo a   // 0
offset_of Foo b   // 8
```

Takes alignment and reordering into account. The result matches the ABI used
in generated machine code.

### `align_of`

Pushes the alignment of a type:

```gofra
align_of <Type>
```

```gofra
align_of Foo        // 8
align_of int        // 8
align_of char       // 1
align_of int[32]    // 8 — alignment of `int`
```

## Generic structures

A struct can be parameterized by a type:

```gofra
struct Generic{T}
    field_a T
    field_b T
    field_c int
end

var x Generic{T = int}
```
