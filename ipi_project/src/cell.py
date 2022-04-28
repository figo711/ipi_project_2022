"""
fichier: cell.py
date de création: 28/04/2022
par: `log2git`
"""

from src.utils import Vector

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