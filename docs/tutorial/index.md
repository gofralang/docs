# Getting started

This tutorial walks you through your first Gofra program. By the end, you will
have compiled and run a working binary.

/// note | Not installed yet?
See [Install Gofra](../how-to/installation.md) first.
///

## Step 1: write a program

Create `hello.gof`:

```gofra
#include "std"

func void main[]
    "Hello, World!" println
end
```

## Step 2: compile and run

```bash
gofra run hello.gof
```

You should see:

```
Hello, World!
```

## What just happened

- `#include "std"` includes required `println`

- `func void main[]` declares the entry point.
- `"Hello, World!"` pushes a string onto the stack.
- `println` pops it and writes it to stdout.
