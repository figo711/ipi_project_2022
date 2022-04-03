#! usr/bin/python3

"""
fichier: fsm.py
date de creation: 31/03/2022
par: `log2git`
"""

from typing import Any, Callable, List, Tuple, Optional, Dict
import time

import src.result as Re

State = Tuple[str, Callable[[Any | None], None]]
Transition = Tuple[str, str, Callable[[Any | None], bool]]
FSM = Dict[str, List[State], List[Transition]]

_attrs = { 'current', 'states', 'transitions' }
_defaults = [ None, [], {} ]

def assert_klass(klass: FSM) -> None:
    assert 'current' in klass, 'current key missing'
    assert 'states' in klass, 'states key missing'
    assert 'transitions' in klass, 'transitions key missing'

def assert_state(st: State) -> None:
    assert isinstance(st, tuple), 'state must be a tuple-typed.'
    assert len(st) == 2, 'state bad size.'
    assert isinstance(st[0], str), 'state name must be a str.'
    assert callable(st[1]), 'state func must be callable.'

def assert_transition(tr: Transition) -> None:
    assert isinstance(tr, tuple), 'transition must be a tuple-typed.'
    assert len(tr) == 3, 'transition bad size.'
    assert isinstance(tr[0], str) and isinstance(tr[1], str), 'transitions indexes must be an str.'
    assert callable(tr[2]), 'transition func must be callable.'

### current functions
def get_current(sm: FSM) -> State:
    """
    Returns current state.
    """
    assert_klass(sm)
    
    result = get_state_by_key(sm, sm['current'])
    assert Re.ok(result), 'get_current, cannot find current state object.'
    return Re.data(result)

def set_current(sm: FSM, name: str) -> None:
    """
    Update current state.
    """
    assert_klass(sm)

    for _, v in enumerate(sm['states']):
        if get_state_name(v) == name:
            sm['current'] = name
            break

def modify_current(sm: FSM, data = None) -> bool:
    """
    Perform a transition between current and next state.
    Returns a flag which indicate if a modification has done.
    """
    assert_klass(sm)

    for t in sm['transitions']:
        if get_transition_name(t, 'first') == get_current(sm) and ( get_transition_func(t)(data) ): # validate by a function
            set_current(sm, get_transition_name(t, 'second'))
            return True
    return False

### states functions
def get_states(sm: FSM) -> List[State]:
    """
    Returns a list of states.
    """
    assert_klass(sm)

    return sm['states']

def get_state_by_key(sm: FSM, key: str): # -> Result
    """
    Returns a state by provided key.
    """

    v = key in get_states(sm)
    d = sm['states'][key] if v else None
    return Re.make(code=v, data=d)

def get_state_name(st: State) -> str:
    """
    Returns the name of the state.
    """
    assert_state(st)

    return st[0]

def get_state_func(st: State) -> Callable[[Any | None], None]:
    """
    Returns the function of the state.
    """
    assert_state(st)

    return st[1]

def add_state(sm: FSM, name: str, func: Callable[[Any | None], None]) -> None:
    """
    Adds the new state (with a name and a func).
    """
    assert_klass(sm)

    sm['states'].append( (name, func) )

### transitions functions
def get_transitions(sm: FSM) -> List[Transition]:
    """
    Returns a list of transitions.
    """
    assert_klass(sm)

    return sm['transitions']

def get_transition_name(tr: Transition, which: str) -> str:
    """
    Returns the name of state from the transition, 
    `which` parameter indicates which state name
    to return.
    """
    assert which in ['first', 'second'], 'which parameter bad value.'
    assert_transition(tr)

    if which == 'first': return tr[0]
    if which == 'second': return tr[1]

def get_transition_func(tr: Transition) -> Callable[[Any | None], bool]:
    """
    Returns the func of the transition.
    """
    assert_transition(tr)

    return tr[2]

def add_transition(sm, current: str, next: str, func: Callable[[Any | None], bool]) -> None:
    """
    Adds the new transition (between current and next state with a func).
    """
    assert_klass(sm)

    current_state_found = False
    next_state_found = False
    index_current = 0
    index_next = 0

    for k, v in enumerate(get_states(sm)):
        st_name = get_state_name(v) 
        if st_name == current:
            current_state_found = True
            index_current = k
        elif st_name == next:
            next_state_found = True
            index_next = k
        
        if current_state_found and next_state_found:
            break
    
    sm['transitions'].append( ( index_current, index_next, func ) )

### display
def display(sm: dict) -> str:
    """
    Returns printable FSM.
    """
    assert_klass(sm)
    
    # TODO: Box constructor
    msg   = '+--- FSM ---+'
    msg += f"| Cur: {sm['current']} |"
    msg += f"| Sta: {''.join(get_state_name(st) for st in get_states(sm))} |"
    msg += f"| Tra: {get_transitions()} |" # TODO: add display transitions (a -> b, b -> c) 
    msg += f"+-----------+"

    return msg