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

from collections import namedtuple

Result = namedtuple('Result', 'code data msg')
OK = 'OK'
ERR = 'ERR'

def make_ok(data) -> Result:
    return make(code=OK, data=data)

def make_err(msg) -> Result:
    return make(code=ERR, msg=msg)

def make(code: str, data = None, msg: str = '') -> Result:
    _result = Result(code, data, msg)
    return _result

def ok(result: Result) -> bool:
    return result.code == OK
