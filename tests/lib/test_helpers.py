from animal import Animal
from world import World


class Bunch():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def create_test_world():
    return World()


def create_test_animal(x_pos=3, y_pos=3, speed=1):
    world = create_test_world()
    return Animal(world, x_pos, y_pos, speed)
