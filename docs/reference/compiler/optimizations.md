# Optimizations

Gofra's optimizer applies the following passes. Each pass has a minimum
optimization level and can be toggled individually.

## Levels

| Level | Passes                    |
| ----- | ------------------------- |
| `-O0` | none (default)            |
| `-O1` | DCE, function inlining    |
| `-O2` | `-O1` + additional passes |

## Passes

| Pass              | Min level | Flag                                           | Impact                                |
| ----------------- | --------- | ---------------------------------------------- | ------------------------------------- |
| DCE               | `-O1`     | `-fdce` / `-fno-dce`                           | Reduced binary size                   |
| Function inlining | `-O1`     | `-finline-functions` / `-fno-inline-functions` | Increased size, increased performance |
