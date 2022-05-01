"""
fichier: session.py
date de création: 28/04/2022
par: `log2git`
"""

from ipi_project.src.utils import assert_definition
from src.systems import make_by_definition, make_copy, FSM
import src.species as Species
import src.grid as Grid

__DEFINITION__ = [ 'day', 'period', 'day_night', 'score', 'player', 'world' ]
__NAME__ = 'Session'

PERIODS = [ 'winter', 'spring', 'summer', 'autumn' ]

def get_definition():
    r = {
        'day': -1,                  # le nombre des jours
        'period': -1,               # ete, hiver, printemps, automne
        'day_night': True,          # true - jour, false - night
        'score': -1, 
        'player': make_copy(Species),
        'world': make_copy(Grid),
        'activity': make_copy(FSM)
    }
    return r

def init(player: Species, grid: Grid):
    s = make_by_definition(get_definition())
    set_day(s, 1)
    set_period(s, PERIODS.index('spring'))
    set_daylight(s, True)
    set_score(s, 0)
    set_player(s, player)
    set_world(s, grid)
    act = make_copy(FSM)
    # FSM.add_state(act, 'activated', <>)
    # FSM.add_state(act, 'paused', <>)
    # FSM.add_state(act, 'idle', <>)



def set_day(kl: dict, day_number: int) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['day'] = int(day_number)

def get_day(kl: dict) -> int:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return int(kl['day'])

def set_period(kl: dict, period_id: int) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    if period_id > 0 and period_id < len(PERIODS) - 1:
        kl['period'] = int(period_id)

def get_period(kl: dict) -> int:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return int(kl['period'])

def get_period_text(kl: dict) -> str:
    return PERIODS[get_period(kl)]

def set_daylight(kl: dict, day: bool) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['day_night'] = bool(day)

def is_daylight(kl: dict) -> bool:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return bool(kl['day_night'])

def set_score(kl: dict, score_value: int) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['score'] = int(score_value)

def get_score(kl: dict) -> int:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return int(kl['score'])

def set_player(kl: dict, player: Species) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['player'] = player

def get_player(kl: dict) -> Species:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return kl['player']

def set_world(kl: dict, world_grid: Grid) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['world'] = world_grid

def get_world(kl: dict) -> Grid:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return kl['world']

def set_activity(kl: dict, act: FSM) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['activity'] = act

def get_activity(kl: dict) -> FSM:
    assert_definition(kl, __DEFINITION__, __NAME__)
    
    return kl['activity']