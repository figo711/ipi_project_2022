#! usr/bin/python3

"""
fichier: fsm.py
date de creation: 31/03/2022
dernier màj: 10/04/2022
par: `log2git`
"""

from typing import Any, Callable, List, Tuple, Optional, Dict

import src.utils.result as Re

State = Tuple[str, Callable[[Any], None]]
Transition = Tuple[str, str, Callable[[Any], bool]]

_attrs = [ 'current', 'states', 'transitions' ]
_defaults = [ None, [], [] ]

def assert_klass(klass: dict) -> None:
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
def get_current(sm: dict) -> State:
    """
    Returns current state.
    """
    assert_klass(sm)
    
    result = get_state_by_key(sm, sm['current'])
    assert Re.ok(result), f'get_current, cannot find current state object. {Re.msg(result)}'
    return Re.data(result)

def set_current(sm: dict, name: str) -> None:
    """
    Update current state.
    """
    assert_klass(sm)

    for _, v in enumerate(sm['states']):
        if get_state_name(v) == name:
            sm['current'] = name
            break

def modify_current(sm: dict, data = None) -> bool:
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
def get_states(sm: dict) -> List[State]:
    """
    Returns a list of states.
    """
    assert_klass(sm)

    return sm['states']

def get_state_by_key(sm: dict, key: str): # -> Result
    """
    Returns a state by provided key.
    """
    
    for state in get_states(sm):
        if get_state_name(state) == key:
            return Re.make_ok(state)
    return Re.make_err(f'State with key `{key}` not found.')

def get_state_name(st: State) -> str:
    """
    Returns the name of the state.
    """
    assert_state(st)

    return st[0]

def get_state_func(st: State) -> Callable[[Any], None]:
    """
    Returns the function of the state.
    """
    assert_state(st)

    return st[1]

def add_state(sm: dict, name: str, func: Callable[[Any], None]) -> None:
    """
    Adds the new state (with a name and a func).
    """
    assert_klass(sm)

    sm['states'].append( (name, func) )

### transitions functions
def get_transitions(sm: dict) -> List[Transition]:
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

def get_transition_func(tr: Transition) -> Callable[[Any], bool]:
    """
    Returns the func of the transition.
    """
    assert_transition(tr)

    return tr[2]

def add_transition(sm: dict, current: str, next: str, func: Callable[[Any], bool]) -> None:
    """
    Adds the new transition (between current and next state with a func).
    """
    assert_klass(sm)

    current_state_found = False
    next_state_found = False

    for k, v in enumerate(get_states(sm)):
        st_name = get_state_name(v) 
        if st_name == current:
            current_state_found = True
        elif st_name == next:
            next_state_found = True
        
        if current_state_found and next_state_found:
            break
    
    assert current_state_found, f'current state: {current} not found. Cannot make a transition.'
    assert next_state_found, f'next state: {next} not found. Cannot make a transition.'
    sm['transitions'].append( ( current, next, func ) )

### display
def display(sm: dict) -> str:
    """
    Returns printable FSM.
    """
    assert_klass(sm)
    
    # TODO: Box constructor
    msg   = '+--- FSM ---+'
    if sm['current']: msg += f"| Cur: {get_state_name(get_current(sm))} |"
    msg += f"| Sta: {''.join(get_state_name(st) for st in get_states(sm))} |"
    msg += f"| Tra: {get_transitions(sm)} |" # TODO: add display transitions (a -> b, b -> c) 
    msg += f"+-----------+"

    return msg