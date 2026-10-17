# Functions and function pointers

In Gofra, functions can be referenced through function pointers. A function
pointer is a first-class value: it can be assigned to variables, passed as
arguments, and called.

## Function type

A function type is written `func <ret> _[<params>]`. The `_` is a placeholder
for the function name — otherwise name will be dropped, so it is useless.

```gofra
func void _[]           // () -> void
func i64 _[i64, i64]    // (i64, i64) -> i64
```

## Type aliases

Use `type` to give a function type a name:

```gofra
type FunctionType func void _[]

var x FunctionType;
var v func void _[];    // same type, written inline
```

## Getting a function pointer

`pointer_of_proc` pushes a pointer to the given function onto the stack:

```gofra
func void f[]
    // ...
end

pointer_of_proc f    // *func void _[]
```

## Calling a function through a pointer

To call a function through a variable, use `call`:

```gofra
func void f[]
    // ...
end

func void main[]
    var v func void _[];

    &v pointer_of_proc f !<

    call v
end
```
