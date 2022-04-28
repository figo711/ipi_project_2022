"""
fichier: species.py
date de création: 28/04/2022
par: `log2git`
"""

from src.systems import FSM, make_copy
import src.mind as Mind

__DEFINITION__ = [ 'age', 'type', 'health', 'damage', 'energy', 'state', 'mind' ]
__NAME__ = 'Species'

def get_definition():
    r = {
        'age': -1,
        'type': -1,
        'health': -1,
        'damage': -1,
        'energy': -1,
        'state': make_copy(FSM),
        'mind': make_copy(Mind)
    }
    return r