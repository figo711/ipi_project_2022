#! usr/bin/python3

"""
fichier: vector.py
date de creation: 15/04/2022
par `log2git`
"""

import math
from collections import namedtuple

Vector = namedtuple('Vector', 'x y')

def make_zero() -> Vector:
    return make(0, 0)

def make_one() -> Vector:
    return make(1, 1)

def make_down() -> Vector:
    return make(0, -1)

def make_left() -> Vector:
    return make(-1, 0)

def make_right() -> Vector:
    return make(1, 0)

def make_up() -> Vector:
    return make(0, 1)

def make(_x: int, _y: int) -> Vector:
    _vec = Vector(_x, _y)
    return _vec

def add(_vec1: Vector, _vec2: Vector) -> Vector:
    _vec3 = make(_vec1.x + _vec2.x, _vec1.y + _vec2.y)
    return _vec3

def substract(_vec1: Vector, _vec2: Vector) -> Vector:
    _vec3 = make(_vec1.x - _vec2.x, _vec1.y - _vec2.y)
    return _vec3

def multiply(_vec1: Vector, _k: int) -> Vector:
    _vec2 = make(_vec1.x * _k, _vec2.y * _k)
    return _vec2

def distance(_vec1: Vector, _vec2: Vector) -> float:
    dx = _vec1.x - _vec2.x
    dy = _vec1.y - _vec2.y
    dist = (dx ** 2 + dy ** 2) ** (1/2)
    return dist

def equals(_vec1: Vector, _vec2: Vector) -> bool:
    return _vec1.x == _vec2.x and _vec1.y == _vec2.y

def display(_vec: dict) -> str:
    return f'[{ _vec.x }, { _vec.y }]'