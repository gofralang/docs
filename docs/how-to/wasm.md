# Compile and run for WebAssembly

This guide shows how to compile a Gofra program to WebAssembly and run it in a
WASM runtime.

For background on WASM, see [wasm.org](https://webassembly.org/)

## Compile to WASM

Use `--target wasm` (or `-t wasm`):

```bash
gofra build hello_world.gof -t wasm -of object
```

This emits `hello_world.wasm`.

/// warning | `-of object` is required
The WASM target does not support `-of executable`: WASM is not an
executable format on its own. It must be loaded by a runtime.
///

## Run the artifact

A `.wasm` file needs a loader. The compiler repository includes a Node.js loader:

```
examples/wasm/node_example_loader.js
```

Run it with:

```bash
node examples/wasm/node_example_loader.js hello_world.wasm
```

/// note | Browser
The same loader logic works in a browser with minor changes to how the
`.wasm` file is fetched. See `examples/wasm/example_wasm_raylib_layer_loader.html`
for a browser example with graphics.
///
