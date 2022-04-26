#! /usr/bin/python3

"""
fichier: save.py
date de création: 26/03/2022
par `log2git`
"""

from typing import Dict
import json
from pathlib import Path

BASE_FOLDER = './assets/saves/'

SAVE_MODE = {
    'json': {
        'name': 'JSON',
        'ext': '.json',
        'func': lambda X: json.dumps(X, sort_keys = True, indent = 4),
        'savename': lambda Name: f'{Name}.{SAVE_MODE["json"]["ext"]}',
        'loadfunc': lambda X: json.loads(X)
    },
    'screen': {
        'name': 'SCREEN',
        'ext': '.tx1',
        'func': lambda X: print('nothing'), # screenshotter.take_screen()
        'savename': lambda Name: str(Name) # screenshotter.savefilename()
    }
}

SaveModeEnum = dict # should change next updates...
SaveSystem = Dict[str, SaveModeEnum, dict]

def get_definition() -> SaveSystem:
    return { 'filename': 'standart_save', 'mode': SAVE_MODE['json'], 'data': {} }

def assert_klass(klass: SaveSystem) -> None:
    assert 'filename' in klass, 'filename key missing'
    assert 'mode' in klass, 'mode key missing'
    assert 'data' in klass, 'data key missing'

### filename
def get_filename(ss: SaveSystem) -> str:
    """
    Returns save file name.
    """
    assert_klass(ss)

    return ss['filename']

### mode
def get_mode(ss: SaveSystem) -> SaveModeEnum:
    """
    Returns save mode.
    """
    assert_klass(ss)

    return ss['mode']

### data
def get_data(ss: SaveSystem) -> dict:
    """
    Returns stored data.
    """
    assert_klass(ss)

    return ss['data']

def set_data(ss: SaveSystem, data: dict) -> None:
    """
    Updates stored data.
    """
    assert_klass(ss)

    ss['data'] = data

def save_data(ss: SaveSystem) -> None:
    """
    Saves stored data into a file.
    """
    assert_klass(ss)

    _mode = get_mode(ss)
    _mode_name, _callback, _sname = _mode['name'], _mode['ext'], _mode['func'], _mode['savename']
    _data = get_data(ss)
    _fname = get_filename(ss)
    print(f'Using {_mode_name}...')
    _r = _callback(_data)
    write_into(_r, _sname(_fname)) 
    # screenshotter.save(result_scr, True) 
    # true pour stardart name (CaptureDuJeu_ANNEE.MOIS.JOUR_HEURE.MINUTE.SECONDE.txt)

def load_data(ss: SaveSystem) -> None:
    """
    Loads the data from the file.
    """
    assert_klass(ss)

    _mode = get_mode(ss)
    _load, _namesave = _mode['loadfunc'], _mode['savename']
    _fname = get_filename(ss)
    _r = read_from(_namesave(_fname))
    _data = _load(_r)
    set_data(ss, _data)
    if get_data(ss) != None: 
        print(f"LOADED Data < {display(ss)} > => | {_data} |")

### internal methods
def write_into(data_str: str, final_name: str) -> None:
    """
    Utility method, writes a str-object into a file.
    """

    with open(construct_path(final_name), 'w') as f:
        f.write(data_str)

def read_from(name: str) -> str:
    """
    Utility method, reads and returns content of a file.
    """

    _out = ''
    with open(construct_path(name), 'r') as f:
        _out = f.readlines() # TODO: review
    return _out

def construct_path(filename: str) -> str:
    """
    Utility method, build a path for write/read methods.
    """
    p = Path(BASE_FOLDER)
    q = p / filename

### display
def display(ss: SaveSystem) -> str:
    """
    Returns printable SaveSystem.
    """
    assert_klass(ss)

    _fname = get_filename(ss)
    _mode = get_mode(ss)
    _mode_name = _mode['name']
    return f'SaveSystem{_mode_name} [Name: {_fname}]'