# Toolchain (compiler) architecture

This page describes the internal structure of the Gofra compiler. It is
intended for contributors and advanced users.

## Components

The toolchain consists of:

| Component      | Role                                  |
| -------------- | ------------------------------------- |
| CLI            | Parses arguments, drives the pipeline |
| Lexer          | Source text → tokens                  |
| Preprocessor   | Resolves `#`-directives on tokens     |
| Parser         | Tokens → HIR                          |
| Type checker   | Validates HIR types                   |
| Optimizer      | HIR passes                            |
| Code generator | HIR → assembly                        |
| Assembler      | Assembly → object file                |
| Linker         | Object files → binary                 |

## Pipeline

```
CLI
 → Lexer
 → Preprocessor
 → Parser
 → Optimizer
 → Type checker
 → Code generator
 → Assembler
 → Linker
```

## Code generation

By default, all architectures emit **assembly** (near-machine code). The
assembler turns it into binary machine code.

This two-step design has a few advantages:

- The code generator is simpler — it emits text, not bytes.
- The assembly can be inspected and debugged.
- The assembler handles encoding, relocation, and platform-specific details.

## HIR and type checking

The parser produces an **HIR** (High-level IR) and performs minimal type
checking. A separate **type checker** module validates that types are
compatible within operations (arithmetic, function calls, etc.).

## Intermediate representations

| IR     | Produced by | Consumed by                      |
| ------ | ----------- | -------------------------------- |
| Tokens | Lexer       | Preprocessor, Parser             |
| HIR    | Parser      | Type checker, Optimizer, Codegen |
