# Variables

A variable is a named container for a value of a specific type. Variables can
be **local** (inside a function) or **global** (at top level).

## Declaration

```gofra
var <name> <type>
```

Examples:

```gofra
var x int
var c char
var p *int
var a int[32]
```

The type is required unless an initializer allows inference (see below).

## Initializers

A variable can be initialized at declaration:

```gofra
var x int = 10
var c char = 'a'
var s *string = "Hello, World"
var a int[3] = [1, 2, 3]
```

## Type inference

If the initializer determines the type unambiguously, the type may be omitted:

```gofra
var x = 5                  // int
var s = "test"             // *string
var a = [1, 2, 3]          // int[3]
var a int[] = [1, 2, 3]    // int[3], unfinished -> finished declaration

```

Ambiguous initializers require an explicit type:

```gofra
var e = []    // error: cannot infer element type
```

## Constants

A variable with a compile-time known initializer can be declared `const`:

```gofra
const x = 5
const y int = 10
```

A constant:

- Cannot be modified after declaration.
- Cannot have its address taken (`&x` is an error).
- May be inlined and eliminated by the optimizer.

```gofra
const x = 5

&x         // error: cannot take address of a constant
```

## Storage duration

The storage duration of a variable depends on where it is declared:

| Where             | Storage                 | Initialization                                  |
| ----------------- | ----------------------- | ----------------------------------------------- |
| Top level         | Global (static segment) | Zero-initialized                                |
| Inside a function | Local (stack)           | Uninitialized unless initialized at declaration |

```gofra
var global int    // zero-initialized

func void main[]
    var local int    // uninitialized
end
```
