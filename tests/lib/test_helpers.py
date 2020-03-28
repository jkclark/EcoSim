from world import World


class Bunch():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def create_test_world():
    return World()
