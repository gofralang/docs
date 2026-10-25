# Attributes

Attribute in _Gofra_ is an keyword that is applied to _object_ (function, variable, type)

## Function attributes

### `pub`

Applies to: `functions`

Mark function as exposed to other modules, and exposed inside compiled object file as function symbol for later linking

Example for module system:

```gofra
// mod.gof:
pub func f[]
end

// When importing module with this function, it allows to call and use that function in any way:

import mod;
call mod.f
```

Example for object file linkage:

```gofra
pub func f[]
end

// When compiling down to object file,
// symbol `f` remains public, and you can link that object file with other objects that externs `f` at linkage
```

### `naked`

Applies to: `functions`

Naked functions does not have _prologue_ and _epilogue_ in machine code nor any compiled inserted code, they contains only assembly instructions.

They allows to write functions which will be broken due to compiler inserted code

For example:

```gofra
naked func void f[]
    // no prologue
    inline_raw_asm "{machine_instructions}"
    inline_raw_asm "ret"
    // no epilogue
end
```

Notice: as compiler cannot insert boilerplate instructions into these functions, you must comply with return logic (link-registers) and manage arguments by own, naked functions supports parameters but it is only for type checking and calling convention only

### `no_mangle`

Applies to: `functions`

Disables name mangling for the symbol. The symbol in the produced object file
is exactly the identifier written in source — without module prefix, kind
suffix

```gofra
no_mangle func void gofra_init[]
    // ...
end
// Symbol in object file: `gofra_init`
// C: void gofra_init(void);
```

Notice: `extern` functions and variables already imply `no_mangle` — they use
the C ABI and are resolved by their literal name. Writing `no_mangle` on an
`extern` declaration is redundant and emits a warning.

### `extern`

Applies to: `functions`

Mark function as defined somewhere else and not in produced artifact (object file, executable), for later linking with library/object file.

Those functions cannot have any body/operators inside it.

For example external function `puts` from `libc` library is declared as:

```gofra
extern func int _puts[*char[]]
```

Compiler will try its best to perform such call assuming _Gofra_/_C_ call convention / ABI

[Read more about FFI...](../how-to/ffi.md)

### `inline`

Applies to: `functions`

Functions that marked as `inline` has no real call, it _unwraps_ its _body_ directly from direct call (inside caller)

Compiler tries to apply these attributes to inlineable functions via heuristics while inline optimizations are enabled

For example:

```gofra
func int f[]
    32 return
end

// On non inline call:
f return // yields 32

// If there is `inline` attribute
32 return // yields 32, expanded from inline function

```

[Read more about optimizations...](../explanation/compiler/optimizations.md)

### `no_return`

Applies to: `functions`

Mark function as having no possible way out, for example `exit` system function, these function must has no return value

Compiler will warn you if you have function that always calls to `no_return` functions
Attribute allows to emit general compiler warnings and errors and perform possible optimizations,
mostly used in compiler library, but useful if you calling `exit` function and has nothing more

This checks ran only at compile-time and has no effect on runtime

```gofra
no_return func void x[]
    // Must has no way out
end

func void x1[]
   call exit // warning, always calling to `no_return` function - propagate attribute

   2 2 + drop // warning, unreachable code, and allows to apply optimizations like DCE
end

func void x1[]
    false if ==
        call exit // may have conditional `no_return` calls without any warning
    end
end
```

## Structure attributes

### `reorder`

Applies to: `structures`

Apply reordering to structure.
Reordering is a process when for performance reasons,
fields of structure being re-ordered to solve alignment issues (redundant padding on structure memory layout)

By default, structures does not apply reordering, overridde by specifying this attribute.

Compiler will warn you if you have possible reordering on any structure

```gofra
struct bad_layout
    a char // 1 byte
    b int  // 8 byte
    c char // 1 byte
end // Unpacked, 24 bytes

struct reorder reordered_layout
    a char // 1 byte
    b int  // 8 byte
    c char // 1 byte
end // Unpacked, reordered 16 bytes
// Order was transformed into [b, a, c] (int, char, char) re-using padding from int to char
```

### `packed`

Applies to: `structures`

Apply packing to structure.
Packing is a process when compiler removes all padding between fields of structure,
laying them out contiguously in memory without any alignment.

By default, structures are padded to satisfy alignment requirements of their fields.
Override by specifying this attribute.

Compiler will warn you if you have possible packing on any structure

```gofra
struct unpacked_layout
    a char // 1 byte
    b int  // 8 byte, aligned to 8 bytes -> 7 bytes padding before
    c char // 1 byte
end // Padded, 24 bytes

struct packed packed_layout
    a char // 1 byte
    b int  // 8 byte, no padding before
    c char // 1 byte
end // Packed, 10 bytes
// Layout is [a, b, c] with no padding between fields
```
