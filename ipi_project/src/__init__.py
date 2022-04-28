"""
fichier: __init__.py
date de création: 25/03/2022
par: `log2git`
"""

import src.cell as Cell
import src.game as Game
import src.grid as Grid
import src.mind as Mind
import src.resource as Resource
import src.session as Session
import src.species as Species
import src.tree as Tree

def make_copy(system: dict):
    new_system = dict(system.get_definition())
    return new_system