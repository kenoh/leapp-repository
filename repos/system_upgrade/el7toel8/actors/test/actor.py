from leapp.actors import Actor
from leapp.actor.library.a import Ex
from leapp.actor.library.b import func


def Test(Actor):
    name = 'test'

    def process(self):
        print("Id inside actor: %s" % id(Ex))
        try:
            func()
        except Ex:
            print('catched')
        else:
            print('not catched')
