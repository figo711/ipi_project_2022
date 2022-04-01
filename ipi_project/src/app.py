"""
fichier: app.py
date de création: 25/03/2022
par: `log2git`
"""

# LES MODULES INTERNES
import time

_CONFIG = {
    'wait_frame_time': 10, # c'est en microsecondes
}

def launch() -> None:
    """
    Cette fonction va lancer le jeu.
    """
    awake()
    start()
    run_update()
    pass

def wait_frame() -> None:
    """
    Faire une attente pour simuler qui le fait des frames ont ete afficher.
    """
    time.sleep(_CONFIG['wait_frame_time'])
    pass

def run_update() -> None:
    """
    Boucle de simulation.
    """
    while True:
        update()
        wait_frame()
    pass

### LE JEU ###

def awake() -> None:
    """
    Une fonction qui est obligatoirement appelee en premier AVANT la fonction start().
    Cette fonction (awake), est la pour initialiser les parties internes du programmes.
    Retourne rien, seulement du vide(void).
    """
    pass

def start() -> None:
    """
    Au contraire de awake, cette fonction va initialiser les élements du jeu par la
    fonction create respective de chaque module importe.
    Retourne rien, seulement du vide(void).
    """
    pass

def update() -> None:
    """
    Cette fonction doit etre appelee par run_update chaque frame. 
    """
    pass

##############


# TESTS
if __name__ == "__main__":
    # TODO: des tests à mettre...
    pass
