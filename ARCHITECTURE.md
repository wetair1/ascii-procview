# Architecture

ascii-procview is a minimal curses process viewer built with the Python standard library.

## Runtime flow

1. The app scans numeric directories in `/proc`.
2. Each process status file is parsed for name, state and RSS memory.
3. Processes are sorted by memory usage.
4. The curses screen redraws the current process table on each refresh.
5. Pressing `q` exits the app.

## Main parts

- `read_proc()` collects process rows from `/proc/<pid>/status`.
- The process row format is `(rss, pid, state, name)`.
- `draw()` owns the curses loop, refresh timing and keyboard handling.

## Design rules

- Keep dependencies at zero.
- Keep `/proc` parsing small and isolated.
- Ignore processes that disappear while scanning.
- Keep the table readable on narrow terminals.
- Prefer simple polling over background workers.
