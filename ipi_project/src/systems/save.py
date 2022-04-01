#! /usr/bin/python3

"""
fichier: save.py
date de création: 26/03/2022
par `log2git`
"""

import json

from src.klass import klass

BASE_FOLDER = None # il faut la mettre après sinon problematic

def this(save_name, save_mode='json'):
    ss = klass(ss, 'create', save_name=save_name, save_mode=save_mode, on_create=on_create)
    return ss

def on_create(ss, save_name, save_mode):
    klass(ss, 'set', key='save_name', value=save_name)
    klass(ss, 'set', key='save_mode', value=save_mode)
    klass(klass(ss, 'get', key='__base__'), 'set', key='on_display', value=on_display)
    klass(ss, 'set', key='save_data', value={})
    # add methods
    klass(ss, 'set', key='saveData', value=saveDataFunc)

def on_display(ss):
    name = klass(ss, 'get', key='save_name')
    mode = klass(ss, 'get', key='save_mode').upper()
    return f'SaveSystem{mode} [Name: {name}]'

def updateDataFunc(ss, new_date):
    klass(ss, 'set', key='save_date', value=new_data)

def saveDataFunc(ss):
    mode = klass(ss, 'get', key='save_mode')
    data = klass(ss, 'get', key='save_data')
    name = klass(ss, 'get', key='save_name')
    if mode == 'json':
        result_json = json.dumps(data, sort_keys = True, indent = 4)
        writeIntoFile(result_json, f'{SAVEFILENAME}_{name}.json')
    elif mode == 'secret':
        result_sss = secretify.make_ugly(data)
        writeIntoFile(result_sss, secretify.hash_str(SAVEFILENAME))
    elif mode == 'screen': # et oui il est possible de sauvegarder un screenshot (capture du jeu seulement)
        result_scr = screenshotter.take_screen()
        screenshotter.save(result_scr, True) # true pour stardart name (CaptureDuJeu_ANNEE.MOIS.JOUR_HEURE.MINUTE.SECONDE.txt)
    else:
        raise Exception('Undefined save_mode.')

def loadDataFunc(ss):
    mode = klass(ss, 'get', key='save_mode')
    name = klass(ss, 'get', key='save_name')
    if mode == 'json':
        result = readFromFile(f'{SAVEFILENAME}_{name}.json')
        readed_data = json.loads(result)
    elif mode == 'secret':
        result = readFromFile(secretify.hash_str(SAVEFILENAME))
