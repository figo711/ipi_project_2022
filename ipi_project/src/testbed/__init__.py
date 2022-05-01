import curses
import random
from threading import Thread
import time
from curses import textpad


from ..utils import Vector
import src.testbed.player as Player

DIRECTIONS = {
    curses.KEY_UP : Vector.make_up(),
    curses.KEY_DOWN : Vector.make_down(),
    curses.KEY_LEFT : Vector.make_left(),
    curses.KEY_RIGHT : Vector.make_right(),
}

def awake():
    pl = Player.new(15, 15)
    return pl

def loop(stdscr, pl):
    while True:
        key = stdscr.getch()

        if key in DIRECTIONS: 
            Player.set_direction(pl, DIRECTIONS[key])
            Player.move(pl)

def disp_buffer(cbuffer) -> str:
    _buffer = ''
    for line in cbuffer:
        _buffer += ''.join(ch for ch in line)
        # _buffer += '\n'
    return _buffer[:-1]

def main():
    stdscr = curses.initscr()
    stdscr.timeout(500)
    stdscr.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    stdscr.border(0)
    curses.curs_set(0)
    pl = awake()
    # Player.start(pl)
    Thread(target=loop, args=(stdscr,pl,)).start()
    
    try:
        while True:
            stdscr.clear()
            h, w  = stdscr.getmaxyx()

            textpad.rectangle(stdscr, 1, 1, h - 2, w - 2)

            stdscr.addstr(Player.get_position(pl).y, Player.get_position(pl).x, Player.get_shape(pl))
            stdscr.refresh()
            time.sleep(1/60)
    finally:
        stdscr.getch()
        curses.endwin()