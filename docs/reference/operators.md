# Operators

Gofra operators are **postfix**: they follow their operands.

## Arithmetic

| Operator | Mnemonic   | Description    |
| -------- | ---------- | -------------- |
| `+`      | `a b -> c` | addition       |
| `-`      | `a b -> c` | subtraction    |
| `*`      | `a b -> c` | multiplication |
| `/`      | `a b -> c` | division       |
| `%`      | `a b -> c` | modulo         |

```gofra
2 3 +    // 5
10 3 %   // 1
```

## Comparison

| Operator | Mnemonic      | Description      |
| -------- | ------------- | ---------------- |
| `==`     | `a b -> bool` | equal            |
| `!=`     | `a b -> bool` | not equal        |
| `<`      | `a b -> bool` | less than        |
| `>`      | `a b -> bool` | greater than     |
| `<=`     | `a b -> bool` | less or equal    |
| `>=`     | `a b -> bool` | greater or equal |

## Logical

| Operator | Mnemonic            | Description |
| -------- | ------------------- | ----------- |
| `&&`     | `bool bool -> bool` | AND         |
| `\|\|`   | `bool bool -> bool` | OR          |
| `lnot`   | `bool -> bool`      | NOT         |

<!-- TODO: confirm — is NOT `lnot` or `!`? -->

## Bitwise

| Operator | Mnemonic   | Description |
| -------- | ---------- | ----------- |
| `&`      | `a b -> c` | AND         |
| `\|`     | `a b -> c` | OR          |
| `^`      | `a b -> c` | XOR         |
| `<<`     | `a b -> c` | shift left  |
| `>>`     | `a b -> c` | shift right |

```gofra
2 3 <<    // 16
2 3 >>    // 0
2 3 &     // 2
2 3 ^     // 1
```

## Memory

| Operator | Mnemonic          | Description           |
| -------- | ----------------- | --------------------- |
| `!<`     | `addr val -> _ _` | store `val` at `addr` |
| `?>`     | `addr -> val`     | load from `addr`      |

```gofra
var x int
&x 10 !<    // x = 10
&x ?>       // 10
```
