"""
fichier: grid.py
date de création: 28/04/2022
par: `log2git`
"""

from src.utils import Vector

__DEFINITION__ = [ 'cells', 'selected' ]
__NAME__ = 'Grid'

def get_definition():
    r = {
        'cells': [],                        # liste des listes
        'selected': Vector.make_zero()      # case selectionne
    }
    return r