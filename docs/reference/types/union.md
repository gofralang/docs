# Union types

A `union` is an overlapping type: all of its members share the same memory.
Its size is the maximum of all its members' sizes, rounded up to the largest
alignment requirement.

Only one member is meaningful at a time. Writing to one member invalidates the
others.

## Syntax

```gofra
union <Name>
    <field> <Type>
    <field> <Type>
    ...
end
```

## Declaration

```gofra
union MyUnion
    as_2b i16
    as_8b i64
end
```

## Size

The size of a union is the size of its largest member:

```gofra
union MyUnion
    as_2b i16   // 2 bytes
    as_8b i64   // 8 bytes
end
// sizeof MyUnion = 8
```

## Memory layout

All members start at offset `0` and overlap:

```
*MyUnion = [ ...8 bytes... ]
             ^
             all members start here
```

When you access a member, the compiler reads exactly the number of bytes
required by that member's type.

```gofra
union MyUnion
    as_2b i16
    as_8b i64
end
```

## Accessing members

Members are accessed with `.` (dot), same as structures.

```gofra
struct Foo
    a int
    b int
end

struct Bar
    a char
    b char
    c int
end

union MyUnion
    foo Foo
    bar Bar
end

var x MyUnion;
```

Writing to a member:

```gofra
&x.bar.c 10 !<
```

Reading it back:

```gofra
x.bar.c
```

## Ordering and alignment

Field ordering and alignment do not apply to unions. A union uses a single
memory chunk for all variants, so there is nothing to reorder or pad.

As a result:

- `offset_of` any member is `0`.
- `align_of` a union is the **maximum** alignment over all its members.

## Attributes

The following attributes **cannot** be applied to unions:

- [`reorder`](../attributes.md#reorder)
- [`packed`](../attributes.md#packed)

Both are meaningless for a type with overlapping members.

## Examples

### "Type punning"

```gofra
union Bits
    as_int i64
    as_ptr *char[]
end

var b Bits;
42 b.as_int !<
b.as_ptr // *char[]
```
