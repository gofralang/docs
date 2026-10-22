# Editor support

This guide shows how to set up editor support for Gofra.

Editor extensions provide syntax highlighting, indentation, and snippets for
`.gof` files.

## Vim / Neovim

The Gofra plugin for Vim is maintained by
[Stepan Zubkov](https://github.com/stepanzubkov).

**Repository:** [github.com/stepanzubkov/gofra.vim](https://github.com/stepanzubkov/gofra.vim)

### Features

- Syntax highlighting for `.gof` files.
- Automatic indentation.

### Installation

See the repository's README for installation instructions.

## Visual Studio Code

The VS Code extension is not yet on the Marketplace. Install it from source.

**Repository:** [github.com/gofralang/gofra-vscode](https://github.com/gofralang/gofra-vscode)

### Features

- Syntax highlighting for `.gof` files.

### Installation

See the repository's README for installation instructions.

/// note | Marketplace
The extension is planned for the VS Code Marketplace. Until then, install
from source.
///

## Zed

The Zed extension is not yet published in the extension registry. Install it
as a dev extension.

**Repository:** [github.com/gofralang/gofra-zed](https://github.com/gofralang/gofra-zed)

### Features

- Syntax highlighting for `.gof` and `.gofra` files.
- Bracket matching and auto indentation.
- Code outline for functions, structures, unions and type aliases.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gofralang/gofra-zed
   ```

2. In Zed open the extensions panel (`Cmd+Shift+X` / `Ctrl+Shift+X`), click the
   `...` menu and choose **Install Dev Extension**.
3. Select the `gofra-zed` directory.

The syntax highlighting is implemented with a
[tree-sitter](https://tree-sitter.github.io) grammar that lives in
[github.com/gofralang/tree-sitter-gofra](https://github.com/gofralang/tree-sitter-gofra).

## Other editors

If your editor is not listed here, you can write an extension yourself. The
existing implementations are good references
