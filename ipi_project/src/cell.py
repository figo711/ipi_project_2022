"""
fichier: cell.py
date de création: 28/04/2022
par: `log2git`
"""

from src.utils import Vector, assert_definition

__DEFINITION__ = ['position', 'shape', 'temperature', 'extras']
__NAME__ = 'Cell'

def get_definition() -> None:
    r = {
        'position': Vector.make_zero(),
        'shape': '?',
        'temperature': 0,
        'extras': []
    }
    return r

def get_pos(kl: dict) -> Vector.Vector:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return kl['position']

def get_shape(kl: dict) -> str:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return str(kl['shape'])

def set_shape(kl: dict, shape: str) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['shape'] = str(shape)

def get_temp(kl: dict) -> float:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return float(kl['temperature'])

def set_temp(kl: dict, temp: float) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['temperature'] = float(temp)

def get_extras(kl: dict) -> list:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return kl['extras']