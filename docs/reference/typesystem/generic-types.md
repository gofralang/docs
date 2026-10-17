# Generic types

A generic type is a **lazy template** for a concrete type. It is parameterized
by one or more type parameters and is not usable until applied to concrete
types.

## Terminology

| Term            | Example                      | Meaning                             |
| --------------- | ---------------------------- | ----------------------------------- |
| Type parameter  | `T` in `Identity{T}`         | Placeholder for a type              |
| Type argument   | `int` in `Identity{T = int}` | Concrete type bound to a parameter  |
| Generic type    | `Identity{T}`                | Unapplied template                  |
| Applied generic | `Identity{T = int}`          | Concrete type after application     |
| Concrete type   | `int`, `*int`, `int[3]`      | Fully resolved type with known size |

## Concrete types

A **concrete type** has a known size in bytes. It can be used as a variable
type, a struct field type, or a function parameter type.

Primitive types (`int`, `char`, `bool`, …) are concrete. Composite types over
concrete types (`*int`, `int[3]`, `struct Point`) are also concrete.

Generic types are **not** concrete. They cannot be used directly

## Defining a generic type

A generic type is defined with `type` and `=`:

```gofra
type Identity{T} T
type XT{T} *T
type Array{T, N} T[N]
```

A generic struct is defined with `struct`:

```gofra
struct Slice{T, K}
    data *T[K]
    len int
end
```

## Applying a generic type

Applying a generic type to concrete arguments produces a concrete type:

```gofra
type Identity{T} T

var x Identity{T = int}    // typeof(x) is `int`
```

With value arguments:

```gofra
type Array{T, N} T[N]

var arr Array{T = int, N = 3}    // int[3]
```

/// note | Type parameter names are required
Application must name the type parameter: `Identity{T = int}`, not
`Identity{int}`.
///
