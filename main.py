#!/usr/bin/env python3
import curses, os, time


def read_proc():
    rows = []
    for pid in os.listdir('/proc'):
        if not pid.isdigit(): continue
        try:
            status = open(f'/proc/{pid}/status').read().splitlines()
            d = dict(line.split(':',1) for line in status if ':' in line)
            name = d.get('Name','?').strip()
            state = d.get('State','?').strip().split()[0]
            rss = int(d.get('VmRSS','0 kB').strip().split()[0])
            rows.append((rss, int(pid), state, name))
        except Exception:
            pass
    return sorted(rows, reverse=True)


def draw(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    while True:
        rows = read_proc()
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(0, 2, 'ASCII PROCVIEW - top RSS processes - q to quit')
        stdscr.addstr(2, 2, 'RSS MB     PID  S  NAME')
        for i, (rss, pid, state, name) in enumerate(rows[:h-4], 3):
            stdscr.addstr(i, 2, f'{rss/1024:7.1f} {pid:7d}  {state:<1}  {name[:w-25]}')
        for _ in range(10):
            if stdscr.getch() in (ord('q'), ord('Q')): return
            time.sleep(0.1)


if __name__ == '__main__':
    curses.wrapper(draw)
