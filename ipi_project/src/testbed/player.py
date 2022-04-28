import curses

from ..utils import Vector


DIRECTIONS = {
    curses.KEY_UP : Vector.make_up(),
    curses.KEY_DOWN : Vector.make_down(),
    curses.KEY_LEFT : Vector.make_left(),
    curses.KEY_RIGHT : Vector.make_right(),
}

def new(x, y):
    return {'pos':Vector.make(x, y), 'dir':Vector.make_zero()}

def set_position(pl, pos):
    pl['pos'] = pos

def get_position(pl):
    return pl['pos']

def set_direction(pl, dir):
    pl['dir'] = dir

def get_direction(pl):
    return pl['dir']

def move(pl):
    pos = get_position(pl)
    dir = get_direction(pl)
    set_position(pl, Vector.add(pos, dir))
    set_direction(pl, Vector.make_zero())

def update(pl, stdscr):
    key = stdscr.getch()
    new_pos = DIRECTIONS.get(key)
    if new_pos: set_direction(pl, new_pos)
    move(pl)