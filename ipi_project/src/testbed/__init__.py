import curses
import random
import time

import src.testbed.player as Player

def init():
    curses.curs_set(0)

def awake():
    pl = Player.new(15, 15)
    return pl

def realmain(stdscr):
    init()
    stdscr.border(0)
    pl = awake()
    h, w = stdscr.getmaxyx()
    
    # for i in range(h * w - 1):
    #     screen_buffer += chr(random.randint(50, 126))
    stdscr.clear()
    stdscr.timeout(10)
    while True:
        screen_buffer = [[' ' for x in range(w)] for y in range(h)] 
        key = stdscr.getch()
        if key == ord('q'): break
        Player.update(pl, stdscr)
        # ... need thread impl
        stdscr.clear()

        stdscr.border(0)
        Player.draw(pl, screen_buffer)

        ff = disp_buffer(screen_buffer)
        assert len(ff) == h * w - 1, f'Error {len(ff)} and {h * w - 1}'
        stdscr.addstr(ff)
        stdscr.refresh()

    stdscr.getch()

def disp_buffer(cbuffer) -> str:
    _buffer = ''
    for line in cbuffer:
        _buffer += ''.join(ch for ch in line)
        # _buffer += '\n'
    return _buffer[:-1]

def main():
    curses.wrapper(realmain)