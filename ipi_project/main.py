#! usr/bin/python3

"""
fichier: main.py
date de création: 25/03/2022
par: `log2git`
"""

# import src.game
import src.testbed as testbed

def main():
    """
    Démarre le jeu au faisant un appel à une fonction du module `lejeu`.
    Retourne rien, seulement du vide (void).
    """
    src.game.launch() # On appele launch() pour allumer le jeu.

if __name__ == '__main__':
    """
    C'est ici que le programme fait son premier appel à une fonction.
    """
    testbed.main()
    # main()

