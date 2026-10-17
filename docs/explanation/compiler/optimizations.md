# Optimizer and optimizations

Gofra has a built-in optimizer that runs from top-level HIR passes down to
low-level LIR passes, according to the selected target.

This page explains **how the optimizer works and why** it makes the choices it
does. For the list of flags and levels, see the
[reference](../../reference/compiler/optimizations.md).

## Why the optimizer is off by default

Optimizations are disabled by default (`-O0`). This is a deliberate choice:

- **Faster builds.** Every pass costs time, and a compiler is run many times
  during development.
- **Easier debugging.** Unoptimized code maps more directly to source. Stack
  traces, breakpoints, and stepping behave predictably.
- **Predictable codegen.** When you are debugging the compiler itself, you want
  to see what the frontend produced, not what the optimizer rewrote it into.

Optimizations are opt-in: `-O1`.

## DCE — Dead Code Elimination

DCE removes functions that are never called. The motivation is simple: most of
a binary's size comes from libraries, and most library functions are never
used by a given program. Removing them shrinks the output significantly.

### Why `pub` functions are kept

A `pub` function is part of the module's public interface. It may be called
from **outside** the current program — by another module, by an FFI consumer,
or by a linker. The optimizer cannot see those callers, so it must assume the
function is used.

### Why DCE iterates

Removing one function may make others unused. If `a` calls `b`, and `a` is
removed, `b` may now be unused too. DCE repeats until no more functions are
removed.

This is a **fixed-point iteration**. The limit (`--dce-max-iterations`) exists
to bound compile time in pathological cases. In practice, 128 iterations is
more than enough — most programs converge in a handful.

## Function inlining

Inlining replaces a call with the function body. The motivation is performance:
it removes call overhead and exposes the body to further optimization (constant
folding, DCE of unused branches, etc.).

### Why only small functions

Inlining every function would explode binary size. The optimizer uses a
heuristic: functions with more operators than
`--inline-functions-max-operators` are not inlined. The threshold trades code
size for speed.

A very high threshold inlines almost everything — useful for benchmarks, bad
for production binaries.

### Why recursion is skipped

Inlining a recursive function does not terminate. Consider:

```gofra
func int fact[int n]
    n 1 <= if
        1 return
    end
    n n 1 - fact * return
end
```

Inlining `fact` into itself produces another `fact` call, which would be
inlined again, forever.

The optimizer detects recursion and skips it. This is why inlining is a
**partial** transformation: some calls remain calls.

### Why iterations matter

Inlining one function may expose new inlineable calls (a function that was
called once is now called from an inlined body). The optimizer re-scans until
no new inlineable calls appear, bounded by
`--inline-functions-max-iterations`.

If the limit is too low, some inline references are left unresolved. At the
assembler stage, these surface as **unknown calls** — the symbol is marked
inline, but the body was never substituted. The fix is to raise the limit; the
cost is a slightly larger binary.
