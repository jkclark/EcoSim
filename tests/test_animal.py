from animal import Animal
from world import World


def create_test_animal():
    world = World()
    animal = Animal(world, 3, 3, 1)
    return animal


def test_spend_energy():
    animal = create_test_animal()
    assert animal.energy == 100
    animal.step()
    assert animal.energy == 90

    animal2 = create_test_animal()
    animal2.speed = 2
    assert animal2.energy == 100
    animal2.move()
    assert animal2.energy == 80
