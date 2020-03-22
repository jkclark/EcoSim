from animal import Animal
from world import World, WorldCell


def create_test_animal():
    world = World()
    animal = Animal(world, 3, 3, 1)
    return animal


def test_step():
    animal = create_test_animal()
    assert animal.location == WorldCell(3, 3, animal.world)
    animal.step()
    assert animal.location in (
        WorldCell(x, y, animal.world)
        for x in range(2, 5)
        for y in range(2, 5)
        if not x == y == 3
    )


# FIXME: This is actually testing the spend-energy part of animal.step.
#        We need to come up with a way of testing spend_energy() on its own.
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
