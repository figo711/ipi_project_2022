"""
fichier: session.py
date de création: 28/04/2022
par: `log2git`
"""

from src.systems import make_copy
import src.species as Species
import src.grid as Grid

__DEFINITION__ = [ 'day', 'period', 'day_night', 'score', 'player', 'world' ]
__NAME__ = 'Session'

def get_definition():
    r = {
        'day': -1,                  # le nombre des jours
        'period': -1,               # ete, hiver, printemps, automne
        'day_night': True,          # true - jour, false - night
        'score': -1, 
        'player': make_copy(Species),
        'world': make_copy(Grid)
    }
    return r