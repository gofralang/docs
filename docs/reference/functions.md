# Functions

A function is a named block of code with parameters and a return type.

## Syntax

```gofra
func <return-type> <name>[<params>]
    <body>
end
```

Parameters are written as `<type> <name>`, separated by commas:

```gofra
func i64 add[i64 a, i64 b]
    a b + return
end
```

## Return type

The return type follows `func`:

```gofra
func void f[]        // returns nothing
func int f[]         // returns int
func *char[] f[]     // returns a C-string pointer
```

A `void` function cannot return a value:

```gofra
func void f[]
    32 return    // error: void function returns a value
end
```

A non-`void` function must return a value:

```gofra
func int f[]
    // error: missing return
end
```

## Calling

A function is called by pushing its arguments onto the stack and then calling
it:

```gofra
2 3 add
```

/// note | `call` is optional
`call f` and `f` are equivalent for direct calls. The `call` keyword is
required only when calling through a **function pointer variable** or using modules:

```gofra
call v      // v is a function pointer variable
call mod.v  // v is a member of `mod` module
```

///

## Parameters

Arguments are passed on the stack, in order. The function pops them according to
its signature into parameter variables.

```gofra
func i64 add[i64 a, i64 b]
    a b + return
end

2 3 add    // 5
```

## `void` functions

A `void` function produces no value:

```gofra
func void print_hello[]
    "hello" print
end

call print_hello
```

## `extern` functions

An `extern` function is declared but not defined in the current compilation unit.
It is resolved at link time:

```gofra
extern func int puts[*char[]]
```

`extern` functions have no body.

See [`extern`](./attributes.md#extern) for details.

## `pub` functions

A `pub` function is exported from the module and emitted as a public symbol:

```gofra
pub func f[]
    // ...
end
```

See [`pub`](./attributes.md#pub) for details.

## Recursion

Functions may call themselves:

```gofra
func i64 fact[i64 n]
    n 1 <= if
        1 return
    end
    n n 1 - fact * return
end
```
