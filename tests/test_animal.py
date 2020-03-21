from animal import Animal
from world import World


def create_test_animal():
    world = World()
    animal = Animal(world.grid, 3, 3, 1)
    return animal


def test_spend_energy():
    animal = create_test_animal()
    pass
