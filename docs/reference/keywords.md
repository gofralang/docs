# Keywords

Reserved words in Gofra. They cannot be used as identifiers.

## Declarations

| Keyword  | Description                     |
| -------- | ------------------------------- |
| `func`   | function declaration            |
| `var`    | variable declaration            |
| `const`  | constant declaration            |
| `struct` | structure declaration           |
| `union`  | union declaration               |
| `type`   | type alias / generic definition |
| `import` | module import                   |

## Attributes

| Keyword     | Applies to | Description          |
| ----------- | ---------- | -------------------- |
| `pub`       | functions  | exported symbol      |
| `extern`    | functions  | externally defined   |
| `inline`    | functions  | inlineable           |
| `naked`     | functions  | no prologue/epilogue |
| `no_return` | functions  | no return path       |
| `packed`    | structures | remove padding       |
| `reorder`   | structures | reorder fields       |

See [Attributes](./attributes.md) for details.

## Control flow

| Keyword | Description                |
| ------- | -------------------------- |
| `if`    | conditional                |
| `else`  | alternative branch         |
| `while` | loop                       |
| `for`   | range loop                 |
| `in`    | range/collection iteration |
| `do`    | loop body marker           |
| `end`   | end of block               |

## Functions and calls

| Keyword           | Description          |
| ----------------- | -------------------- |
| `return`          | return from function |
| `call`            | call a function      |
| `lambda`          | anonymous function   |
| `pointer_of_proc` | function pointer     |

## Memory and types

| Keyword     | Description                 |
| ----------- | --------------------------- |
| `copy`      | duplicate top of stack      |
| `drop`      | drop top of stack           |
| `swap`      | swap top two                |
| `sizeof`    | size of a type              |
| `align_of`  | alignment of a type         |
| `offset_of` | field offset in a structure |
| `typecast`  | explicit cast               |

## System

| Keyword                 | Description                  |
| ----------------------- | ---------------------------- |
| `syscall0` … `syscall6` | system call with N arguments |
| `inline_raw_asm`        | raw assembly                 |
| `compile_error`         | emit a compile-time error    |
| `breakpoint`            | debugger breakpoint          |

## Literals

| Keyword | Description   |
| ------- | ------------- |
| `true`  | boolean true  |
| `false` | boolean false |

## Preprocessor

| Directive  | Description      |
| ---------- | ---------------- |
| `#include` | include a file   |
| `#define`  | define a macro   |
| `#undef`   | undefine a macro |
| `#ifdef`   | if defined       |
| `#ifndef`  | if not defined   |
| `#endif`   | end conditional  |
