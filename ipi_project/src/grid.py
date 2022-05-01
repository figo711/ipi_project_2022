"""
fichier: grid.py
date de création: 28/04/2022
par: `log2git`
"""

from src.utils import Vector, assert_definition
import src.cell as Cell

__DEFINITION__ = [ 'cells', 'selected' ]
__NAME__ = 'Grid'

def get_definition():
    r = {
        'cells': [],                        # liste des listes
        'selected': Vector.make_zero()      # case selectionne
    }
    return r

def get_cells(kl: dict) -> list[list]:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return kl['cells']

def get_from(kl: dict, coord: tuple[int, int]) -> Cell:
    assert_definition(kl, __DEFINITION__, __NAME__)

    cells = get_cells(kl)
    for vline in cells:
        for cell in vline:
            if Vector.equals(Cell.get_pos(cell), Vector.make(coord[0], coord[1])):
                return cell
    return None

def get_selected(kl: dict) -> Vector.Vector:
    assert_definition(kl, __DEFINITION__, __NAME__)

    return kl['selected']

def set_selected(kl: dict, coord: tuple[int, int]) -> None:
    assert_definition(kl, __DEFINITION__, __NAME__)

    kl['selected'] = Vector.make(coord[0], coord[1])