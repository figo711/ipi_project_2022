#! usr/bin/python3

"""
fichier: result.py
date de creation: 01/04/2022
par `log2git`
"""

"""
Note: Très inspiré du Result du langage Rust. ()
Result ou Re, permet d'avoir un objet qui contient le résultat d'une opération
où on n'est pas sûr d'avoir 
"""

### Constants
OK = 'OK'
ERR = 'ERR'

def ok(result):
    if 'code' in result:
        return result['code'] == OK
    else:
        raise Exception('ok, code key missing.')

def data(result):
    if 'data' in result:
        return result['data']
    else:
        raise Exception('data, data key missing.')
