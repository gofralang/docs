# Pointer types

A pointer holds the memory address of another value. Pointer types are written
`*T`, where `T` is the pointee type.

```gofra
*i8       // pointer to i8
*i64      // pointer to i64
*char[]   // pointer to a char array (C-string)
*MyStruct // pointer to MyStruct
```

## Size and alignment

| Type | Size (64-bit) | Alignment |
| ---- | ------------- | --------- |
| `*T` | 8 bytes       | 8         |

/// note | Always 64bit archicture
Compiler supports only 64 bit architectures assumes pointers are always 64 bit
///

## Address-of

The `&` operator takes the address of an lvalue:

```gofra
var x i64 = 120
&x                // *i64
```

Nested fields:

```gofra
struct Point
    x i64
    y i64
end

var p Point
&p.x              // *i64
```

## Dereference

There is no auto-dereference of pointers for raw value, rather you can use this syntax:

```gofra
var x *i64;

x ?> // read
```

## Casts

### Between pointers

Any pointer can be cast to any other pointer with
[`REINTERPRET`](../typesystem/type-casting.md#reinterpret):

```gofra
var x i64 = 120
&x typecast *i8   // *i64 -> *i8
```

### Pointer <-> integer

An integer can be cast to a pointer and back, provided the integer size matches
the pointer size:

```gofra
&x typecast i64   // *i64 -> i64 (64-bit target)
120 typecast *i8  // i64 -> *i8
```
