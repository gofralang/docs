# Command-line interface

The `gofra` command is the entry point to the toolchain.

```bash
gofra <command> [options]
```

## Commands

| Command   | Description                     |
| --------- | ------------------------------- |
| `version` | Show version                    |
| `targets` | List available targets          |
| `run`     | Compile and run a source file   |
| `clean`   | Clean build cache and artifacts |
| `build`   | Compile a source file           |

## `gofra build`

Compile a Gofra source file into an executable, object, or library.

```bash
gofra build [options] <source_file>
```

### Target

| Flag                                                                                                                       | Description                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `--target {amd64-unknown-linux, arm64-apple-darwin, amd64-unknown-windows, wasm32-unknown-none, amd64-apple-darwin, wasm}` | Target triple. Inferred from the host by default. Cross-compilation is not supported. (`-t`) |

### Output

| Flag                                                           | Default      | Description          |
| -------------------------------------------------------------- | ------------ | -------------------- |
| `--output <path>` / `-o`                                       | inferred     | Output file path     |
| `--output-format {object,executable,library,assembly}` / `-of` | `executable` | Output format        |
| `--entry-point <name>`                                         | `main`       | Entry point function |

### Logging

| Flag                               | Description               |
| ---------------------------------- | ------------------------- |
| `--verbose` / `-v`                 | Enable INFO logs          |
| `-vv`                              | Display compiler commands |
| `--no-lint` / `--no-lint-warnings` | Hide linter warnings      |

### Debug

| Flag                     | Description        |
| ------------------------ | ------------------ |
| `--debug-symbols` / `-g` | Emit debug symbols |

### Preprocessor

| Flag                                | Description                        |
| ----------------------------------- | ---------------------------------- |
| `--preprocess-only` / `--pp` / `-P` | Emit preprocessed source to stdout |
| `--include <dir>` / `-i`            | Add an include search directory    |
| `--define [<name>]` / `-D`          | Define a macro (default value `1`) |

### Cache

| Flag                        | Default    | Description            |
| --------------------------- | ---------- | ---------------------- |
| `--cache-dir <dir>` / `-cd` | `./.build` | Cache directory        |
| `--delete-cache` / `-dc`    |            | Delete cache after run |

### Linker

| Flag                                  | Description                       |
| ------------------------------------- | --------------------------------- |
| `--library-search-path <dir>` / `-L`  | Library search path               |
| `--linker-profile {debug,production}` | Linker profile (default: `debug`) |
| `--linker-flag <flag>` / `-alf`       | Additional linker flag            |
| `--library <lib>` / `--lib` / `-l`    | Link against a library            |
| `--linker-backend {gnu-ld, apple-ld}` | Linker backend                    |
| `--linker-executable <path>`          | Linker executable path            |
| `--no-pkgconfig`                      | Disable `pkg-config`              |

### Optimizations

| Flag                                                       | Default     | Description                           |
| ---------------------------------------------------------- | ----------- | ------------------------------------- |
| `-O0`                                                      | yes         | Disable all optimizations             |
| `-O1`                                                      |             | Apply basic optimizations             |
| `-fdce` / `-fno-dce`                                       | on at `-O1` | Enable / disable DCE                  |
| `--dce-max-iterations <N>`                                 |             | Max DCE iterations                    |
| `-finline-functions` / `-fno-inline-functions`             | on at `-O1` | Enable / disable inlining             |
| `--inline-functions-max-operators <N>`                     |             | Max operators for inlineable function |
| `--inline-functions-max-iterations <N>`                    |             | Max inlining iterations               |
| `-fpeephole-isa-optimizer` / `-fno-peephole-isa-optimizer` | on at `-O1` | Peephole ISA optimizer                |
| `-fomit-frame-pointer` / `-fno-omit-frame-pointer`         | on at `-O1` | Omit frame pointer when unused        |

### Codegen

| Flag                                    | Description                        |
| --------------------------------------- | ---------------------------------- |
| `--no-dwarf-cfi` / `--always-dwarf-cfi` | Control DWARF CFI generation       |
| `--no-compiler-comments`                | No comments in assembly            |
| `--no-align-functions`                  | Disable function alignment         |
| `--align-functions <N>`                 | Function alignment in bytes        |
| `--assembler <flags>` / `-Af`           | Additional assembler flags         |
| `--rt-bounds-checks` / `--oob-checks`   | Enable runtime bounds checks (WIP) |

## `gofra run`

Compile and run a source file. Accepts the same options as `build`, plus:

| Flag                                                      | Description                                   |
| --------------------------------------------------------- | --------------------------------------------- |
| `--propagate-execute-child-exit-code` / `--prop-child-ec` | Propagate the child's exit code to the parent |

## `gofra version`

| Flag | Description                       |
| ---- | --------------------------------- |
| `-v` | Display git build commit and date |

## `gofra targets`

| Flag     | Description    |
| -------- | -------------- |
| `--json` | Output as JSON |

## `gofra clean`

| Flag            | Default    | Description     |
| --------------- | ---------- | --------------- |
| `--cache <dir>` | `./.build` | Cache directory |
