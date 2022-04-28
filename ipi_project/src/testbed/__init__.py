import curses

from ..utils import Vector

DIRECTIONS = {
    curses.KEY_UP : Vector.make_up(),
    curses.KEY_DOWN : Vector.make_down(),
    curses.KEY_LEFT : Vector.make_left(),
    curses.KEY_RIGHT : Vector.make_right(),
}

def realmain(stdscr):
    pl = new()
    update(stdscr, pl)

def main():
    curses.wrapper(realmain)

def new():
    r = dict()
    r['pos'] = Vector.make(15, 15)
    return r

def update(win, pl):
    while True:
        handle(win, pl)
        draw(win, pl)

def draw(win, pl):
    win.clear()
    win.addch(pl['pos'].y, pl['pos'].x, 'F')
    win.refresh()


def handle(win, pl):
    dir = get_dir(win, pl)
    move(pl, dir)

def get_dir(win, pl):
    key = win.getch()

    if key not in DIRECTIONS: return None
    return DIRECTIONS[key]

def move(pl, dir):
    pos = pl['pos']
    new_pos = Vector.add(pos, dir)
    pl['pos'] = new_pos