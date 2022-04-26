#! /usr/bin/python3

"""
fichier: test_fsm.py
date de création: 10/04/2022
par: `log2git`
"""

# TODO: finish

import time

from context import src

import src.systems.fsm as FSM
import src.klass.base_definition as klass

def first_state(data): 
    print(f"Action state =({data})")

def second_state(data): 
    print(f"Action state =({data})")

def third_state(data): 
    print(f"Action state =({data})")

def T_first_second(data):
	print("Transition: first_second->false ({data})")
	return False

def T_first_third(data):
	print("Transition: first_third->true ({data})")
	return True

def T_third_first(data):
	print("Transition: third_first->true ({data})")
	return True

def testMain() -> None:
    me = klass.make_klass(FSM._attrs, FSM._defaults)
    print(FSM.display(me))
    print("[ FSM ] Klass created.")
    FSM.add_state(me, 'first', first_state)
    FSM.add_state(me, 'second', second_state)
    FSM.add_state(me, 'third', third_state)
    FSM.set_current(me, 'first')
    print(me)
    print("etat initial: ", FSM.get_current(me))

    FSM.add_transition(me, 'first', 'second', T_first_second)
    FSM.add_transition(me, 'first', 'third', T_first_third)
    FSM.add_transition(me, 'third', 'first', T_third_first)

    i = 3
    while i:
        print("--------step--------")
        FSM.display(me)
        time.sleep(1)
        print("--action:--")
        _curr = FSM.get_current(me)
        FSM.get_state_func(_curr)("test data")
        time.sleep(1)
        print("--transitions:--")
        FSM.modify_current(me, "test data")
        i -= 1
        time.sleep(1)


if __name__ == '__main__':
    testMain()