"""
fihcier: __init__.py
date de création: 28/04/2022
par: `log2git`
"""

import src.utils.vector as Vector
import src.utils.result as Result

def assert_definition(example: dict, definition: list, def_name: str) -> None:
    for k in definition:
        assert k in example, f'`{k}` key missing in {def_name}'