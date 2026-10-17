# Install Gofra from source

This guide shows how to install Gofra for development.

## Requirements

- Python 3.12 or newer.
- [Poetry](https://python-poetry.org).

## Steps

### 1. Clone

```bash
git clone https://github.com/gofralang/gofra.git
cd gofra
```

### 2. Install dependencies

```bash
poetry install --with dev
```

This also installs [Ruff](https://astral.sh/ruff):

```bash
ruff check .
```

### 3. Verify

```bash
python -m gofra version
```

/// note | Local `gofra`
Inside the Poetry environment (`poetry shell`), the local `gofra` command
shadows the system-wide one.
///
