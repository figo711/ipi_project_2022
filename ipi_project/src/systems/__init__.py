"""
fihcier: __init__.py
date de création: 26/03/2022
par: `log2git`
"""

import emitter as Emitter
import fsm as FSM
import inventory as Inventory
import save as Save

__version__ = '1.0.0'

def make_copy(system: dict):
    new_system = dict(system.get_definition())
    return new_system