# Lambdas

A lambda is an anonymous function defined inline. It produces a function
pointer.

## Syntax

```gofra
lambda func <ret> _[<params>]
    <body>
end
```

## Example

```gofra
type F_T func int _[int, int]

func F_T make_adder[]
    lambda func int _[int, int]
        + return
    end
    return
end
```

The lambda produces a function pointer of type `func int _[int, int]`.

## No captures

A lambda **cannot** capture variables from the enclosing function:

```gofra
func F_T make_adder[int n]
    lambda func int _[int]
        n + return    // error: `n` is not captured
    end
    return
end
```
