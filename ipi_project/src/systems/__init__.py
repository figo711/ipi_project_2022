"""
fihcier: __init__.py
date de création: 26/03/2022
par: `log2git`
"""

import src.systems.emitter as Emitter
import src.systems.fsm as FSM
import src.systems.inventory as Inventory
import src.systems.save as Save

__version__ = '1.0.0'

def make_copy(system: dict):
    return make_by_definition(system.get_definition())

def make_by_definition(definition: dict):
    new_system = dict(definition)
    return new_system