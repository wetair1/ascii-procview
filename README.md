# ascii-procview

Minimal ASCII curses process viewer.

## Features

- Lists running processes
- Sorts by RSS memory usage
- Shows PID, state, name and memory
- Refreshes automatically
- Pure Python stdlib

## Usage

```bash
python3 main.py
```

Press `q` to quit.

## Notes

Process data is read from `/proc`, so this is aimed at Linux systems.
