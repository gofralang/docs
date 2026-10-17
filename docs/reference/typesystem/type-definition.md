# Type definition

The `type` keyword creates an alias for an existing type. An alias can be
**plain** (no parameters) or **generic** (with type parameters).

## Syntax

```gofra
type <Name> <TypeExpr>
type <Name>{<T>, <U>} <TypeExpr>
```

## Plain aliases

An alias without type parameters:

```gofra
type MyInt int
type Callback func void _[]
type IntPtr *int
```

## Generic aliases

An alias with type parameters:

```gofra
type Array{T, N} T[N]
type Pointer{T} *T
```

## Rules

- A plain alias is **transparent**: `MyInt` and `int` are the same type at
  compile time. No runtime cost, no new type.
- A generic alias is **monomorphized**: each instantiation produces a separate
  type.
- Aliases cannot be used to create distinct types.
