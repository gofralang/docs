# `void` type

`void` is the **absence of a type**. It is used as the return type of functions
that produce no value.

/// note | Not a value
`void` has no size, no alignment, and no values. It cannot be stored,
passed, or returned. It only marks that a function returns nothing.
///

## Usage

### Function return type

A function with return type `void` produces no value:

```gofra
func void f[]
    // ...
end
```

Calling it leaves nothing on the stack:

```gofra
call f
```

### Untyped pointers

```gofra
var ptr *void; // mark ptr as pointing to *anything*
```

## Rules

- `void` cannot be used as a variable type:

  ```gofra
  var x void   // error
  ```

- `void` cannot be used as a struct or union field type:

  ```gofra
  struct S
      x void   // error
  end
  ```

- `void` cannot be a parameter type:

  ```gofra
  func f[void]   // error
  ```

- A `void` function cannot return a value:

  ```gofra
  func void f[]
      32 return   // error: function returns `void`
  end
  ```

- A non-`void` function must return a value:

  ```gofra
  func int f[]
      // error: missing return
  end
  ```
