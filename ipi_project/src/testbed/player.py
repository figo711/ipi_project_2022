import curses
from threading import Thread
import time

from ..utils import Vector

def new(x, y):
    return {'pos':Vector.make(x, y), 'dir':Vector.make_zero(), 'shape': 'Ü', 'speed': 10}

def start(pl):
    Thread(target=loop, args=(pl,)).start()

def loop(pl):
    #while Session.get_activity(get_session_from(pl)):
    #   if is_alive(pl):
    while True:
        if True:
            move(pl)
        time.sleep(1 / get_speed(pl))

def set_position(pl, pos):
    pl['pos'] = pos

def get_position(pl):
    return pl['pos']

def set_direction(pl, dir):
    pl['dir'] = dir

def get_direction(pl):
    return pl['dir']

def set_speed(pl, speed):
    pl['speed'] = speed

def get_speed(pl):
    return pl['speed']

def set_shape(pl, shape):
    pl['shape'] = shape

def get_shape(pl):
    return pl['shape']

def move(pl):
    pos = get_position(pl)
    dir = get_direction(pl)
    set_position(pl, Vector.add(pos, dir))
    #set_direction(pl, Vector.make_zero())

def draw(pl, buffer):
    pos = get_position(pl)
    buffer[pos.y][pos.x] = get_shape(pl)