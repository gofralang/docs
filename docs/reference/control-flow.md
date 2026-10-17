# Control flow

Gofra provides conditional execution and looping constructs.

## `if`

Executes a block if the condition is `true`.

### Syntax

```gofra
<condition> if
    <body>
end
```

### Example

```gofra
1 1 == if
    "true" print
end
```

### `else`

```gofra
<condition> if
    <then>
else
    <else>
end
```

```gofra
1 0 == if
    "equal" print
else
    "not equal" print
end
```

## `while`

Repeats a block while the condition is `true`.

### Syntax

```gofra
while
    <condition>
do
    <body>
end
```

The condition is evaluated **before** each iteration.

### Example

```gofra
var counter int = 0

while
    counter 10 <
do
    counter print_integer
    &counter counter 1 + !<
end
```

## `for`

Iterates over a range or a array. Ranges are **exclusive** on the upper
bound.

### Range iteration

```gofra
for i in 0..10 do
    // i = 0, 1, 2, ..., 9
end
```

Reversed ranges count down:

```gofra
for i in 10..0 do
    // i = 9, 8, ..., 0
end
```

### Variable bounds

```gofra
var x = 5

for i in 0..x do
    // i = 0, 1, 2, 3, 4
end
```

/// note | Step is always 1
`for` ranges always step by 1 (or −1 for reversed ranges). There is no
custom step.
///

### Iterating arrays

```gofra
var xs = [5, 6, 7]

for i in 0..xs do
    // i = 0, 1, 2 (index)
end

for x in xs do
    // x = *5, *6, *7 (pointer to each element)
end
```

/// note | Pointer iteration
`for x in xs` iterates by **pointer**: `x` is a pointer to the current
element, not a copy of its value.
///

### Lowering

`for i in 0..10` is lowered to:

```gofra
var i int = 0
while
    i 10 <
do
    <body>
    &i i 1 + !<
end
```

For a reversed range (`10..0`), the comparison is `>` and the increment is `-`.
