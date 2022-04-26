#! usr/bin/python3

"""
fichier: emitter.py
date de creation: 25/04/2022
par `log2git`
"""

def assert_emitter(this):
    assert 'events' in this, ''
    assert 'once_events' in this, ''

def get_definition():
    return { 'events': {}, 'once_events': {} }

def on(this, event_name, listener):
    """
    Initialise un nouveau recepteur qui lorsque receverra un signal
    va executer une commande.
    """

    if not event_name or not listener:
        return
    if event_name not in this['events']: 
        this['events'][event_name] = []
    listeners = this['events'].get(event_name)

    if listeners.index(listener) == -1:
        listeners.append(listener)

def once(this, event_name, listener):
    """
    Pareil que `on` sans une repetition de la commande.
    En outre, il execute une seul fois sa commande.
    """

    if not event_name or not listener:
        return

    on(event_name, listener)

    if event_name not in this['once_events']: 
        this['once_events'][event_name] = []
    onceListeners = this['once_events'][event_name]
    onceListeners[listener] = True

def off(this, event_name, listener):
    """
    Eteint le recepteur indique dans la variable listener.
    """

    listeners = this['events'] and this['events'][event_name]
    if not listeners or not len(listeners):
        return
    index = listeners.index(listener)
    if index != -1:
        del listeners[index]

def trigger(this, event_name, *args):
    """
    Envoie un signal, si un recepteur avec le meme event_name
    que le signal alors le recepteur va s'execute
    """
    listeners = this['events'] and this['events'][event_name]
    if not listeners or not len(listeners):
        return
    i = 0
    listener = listeners[i]

    onceListeners = this['once_events'] and this['once_events'][event_name]

    while listener:
        isOnce = onceListeners and onceListeners[listener]
        if isOnce:
            # un listener once doit etre supprimer car il est appele et apres il existe plus.
            off(event_name, listener)
            # la aussi
            del onceListeners[listener]
        # envoi du signal
        listener(args)
        # le recepteur prochain
        i += 0 if isOnce else 1
        listener = listeners[i]