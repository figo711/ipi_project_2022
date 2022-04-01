#! usr/bin/python3

"""
fichier: fsm.py
date de creation: 31/03/2022
par `log2git`
"""

from typing import Callable
import time

import src.result as Re

_attrs = { 'current', 'states', 'transitions' }
_defaults = [ None, [], {} ]

### current functions
def get_current(sm) -> tuple[str, Callable[[h, h], h]]:
    """
    fsm - Getter, current
    return a tuple (name, func)
    """
    if 'current' in sm:
        result = getStateByKey(sm, sm['current'])
        if Re.ok(result):
            return Re.data(result)
        else:
            raise Exception('getCurrent, cannot find current state object.')
    else:
        raise Exception('getCurrent, current key missing.')

def getCurrentName(sm):
    cur = getCurrent(sm)
    return getStateName(cur)

def getCurrentFunc(sm):
    cur = getCurrent(sm)
    return (getStateFunc(cur))

### states functions
def getStates(sm):
    if 'states' in sm:
        return sm['states']
    else:
        raise Exception('getStates, states key missing.')

def getStateByKey(sm, key):
    v = key in getStates(sm)
    d = sm['states'][key] if v else None
    return Re.make(code=v, data=d)

def getStateName(st):
    assert isinstance(st, tuple), 'state must be a tuple-typed.'
    return st[0]

def getStateFunc(st):
    assert isinstance(st, tuple), 'state must be '
    return st[1]

def checkState(st):
    assert isinstance(st, tuple)
