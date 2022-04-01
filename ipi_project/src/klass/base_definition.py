"""
fichier: base_definition.py
date de création: 26/03/2022
par: `log2git`
"""

import src.utils.dict_utils as du

# game = Game.klass()

def klass(objekt, cmd='create', **klass_kwargs):
    """
    Un class vide sans le mot clée `class`, il permet de gérer plus facilement l'abstraction des objets.
    Le paramètre cmd nous permet de dire ce que le klass doit faire, 'create' pour se construire, 'set',
    'get' l'acces et la modification du klass, 'call' pour appel à des méthodes du Klass-héritier et
    'str' pour avoir une conversion klass en str (analogie avec class).
    ---
    Voici un exemple d'utilisation:
        ** Person.py **
        from src.klass import klass

        def this(name, age, id):
            p = klass(p, 'create', name=name, age=age, id=id, on_create=on_create)
            return p

        def on_create(p, **kwargs):
            klass(p, 'set', key='name', value=kwargs.get())

        def on_display(p):
            name = klass
            return f'Person [{k}]'
        ** autre.py **
        person = Person.this(name='Prenom', age=23, id=0) # analogie d'une fonction create()
        value = klass(person, 'get', key='name') # value = Prenom
    """

    def __create__(**kwargs):
        """
        Un create basique qui est commun pour tout objet qui 'hérite' klass.
        """
        objekt_instance = dict()
        objekt_instance['__base__'] = dict()
        if 'on_create' not in objeckt_instance['__base__']: 
            raise Exception('on_create func not found.')
        else:
            objekt_instance['__base__']
            objekt_instance['__base__']['already_created'] = True
        return objekt_instance

    def __set__(objekt, key, value):
        """
        Un mutateur générique, il fonctionne en fonction de la key(clée) et la value(valeur).
        """
        objekt[key] = value 
        # il s'agit aussi d'un __add__ car si key n'existe pas dans objekt, 
        # il sera rajouté dedans avec sa valeur value.

    def __get__(objekt, key):
        """
        Un accesseur générique, il redonne une value(valeur) à partir de la key(clée).
        """
        return du.safe_get(objekt[key]) 
        # safe_get permet de récuper soit la value(valeur) si la key(clée) est dans la liste 
        # sinon un tuple('err', None) donc on pourra eviter de jouer avec le None.

    def __call__(objekt, key, *args):
        """
        Effectue un appel à une fonction qui est stocké dans objekt pour accéder il faut la key(clée).
        Le *args permet de faire passer les arguments s'il y en a.
        """
        # On vérifie que la key(clée) existe et on appelle la fonction (ici x), 
        # sinon on donne l'erreur pour stopper le programme.
        result = du.check(objekt, key, lambda x: x(args), lambda err: "__call__ could not find your func.")

        # Il faut que le résultat soit quelque chose de utile que avoir le None.
        # Remarque: cette vérification ne change rien, la fonction dans tout les cas va retourner le None. :)
        if result not is None: return result

    def __str__(objekt):
        """
        Pour debugger, il est utile d'avoir une belle representation d'un Klass, 
        pour cela on_display doit être défini dans un Klass héritier du klass.
        IMPORTANT: A ne pas confondre avec la fonction pour l'affichage.
        """
        return __call__(objekt, 'on_display')

    # Command parser
    if objekt is None or cmd == 'create':
        objekt = __create__(klass_kwargs)
        return objekt
    elif cmd == 'set':
        __set__(objekt, kwargs['key'], kwargs['value'])
    elif cmd == 'get':
        return __get__(objekt, kwargs['key'])
    elif cmd == 'call':
        return __call__(objekt, kwargs['key'], kwargs['args'])
    elif cmd == 'str':
        return __str__(objekt)
