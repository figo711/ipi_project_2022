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

GAME_ON = False

def awake():
    # init all objects
    pl = Player.new(15, 15)
    return pl

def loop(stdscr, pl):
    # updates, another thread
    global GAME_ON
    while GAME_ON:
        key = stdscr.getch()
        if key == ord('b'):
            GAME_ON = False

        if key in DIRECTIONS: 
            Player.set_direction(pl, DIRECTIONS[key])
            Player.move(pl)
            time.sleep(1/30)

def disp_buffer(cbuffer) -> str:
    _buffer = ''
    for line in cbuffer:
        _buffer += ''.join(ch for ch in line)
        # _buffer += '\n'
    return _buffer[:-1]

def show_gui(stdscr):
    period_text = 'Period: ' + 'Hiver'
    state_text = 'Jour'
    day_text = '154 jours'
    age_text = '145 age'
    score_text = '1000 points'
    stdscr.addstr(1, 2, period_text)
    stdscr.addstr(1, 3 + len(period_text) + 2, state_text)

    # stdscr.addstr(1, 3 + len(period_text) + 2 + len(state_text) + 2, day_text)

def draw(stdscr, pl):
    while GAME_ON:
        stdscr.clear()
        h, w  = stdscr.getmaxyx()

        textpad.rectangle(stdscr, 1, 1, h - 2, w - 2)
        show_gui(stdscr)

        stdscr.addstr(Player.get_position(pl).y, Player.get_position(pl).x, Player.get_shape(pl))
        stdscr.refresh()
        

def main():
    global GAME_ON
    stdscr = curses.initscr()
    stdscr.timeout(500)
    stdscr.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    stdscr.border(0)
    curses.curs_set(0)
    pl = awake()
    GAME_ON = True
    # Player.start(pl)
    Thread(target=loop, args=(stdscr,pl,)).start()
    
    try:
        draw(stdscr, pl)
    finally:
        stdscr.getch()
        curses.endwin()