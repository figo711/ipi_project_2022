"""
fichier: __init__.py
date de création: 25/03/2022
par: `log2git`
"""

import cell as Cell
import game as Game
import grid as Grid
import mind as Mind
import resource as Resource
import session as Session
import species as Species
import tree as Tree

def make_copy(system: dict):
    new_system = dict(system.get_definition())
    return new_system