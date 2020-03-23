from animal import Animal
from world import World, WorldCell


def create_test_animal(x_pos=3, y_pos=3, speed=1):
    world = World()
    animal = Animal(world, x_pos, y_pos, speed)
    return animal


# TODO: We should also check to see if the decorated function gets called or not.
def test_spend_energy_success():
    animal = create_test_animal()

    @Animal.spend_energy(1)
    def test_func(self):
        pass
    setattr(Animal, 'test_func', test_func)

    assert animal.energy == 100
    animal.test_func()
    assert animal.energy == 99


def test_spend_energy_insufficient_energy():
    animal = create_test_animal()

    @Animal.spend_energy(101)
    def test_func(self):
        pass
    setattr(Animal, 'test_func', test_func)

    assert animal.energy == 100
    animal.test_func()
    assert animal.energy == 100


def test_spend_energy_invalid_value():
    animal = create_test_animal()

    @Animal.spend_energy("abc")
    def test_func(self):
        pass
    setattr(Animal, 'test_func', test_func)

    assert animal.energy == 100
    animal.test_func()
    assert animal.energy == 100


def test_step():
    animal = create_test_animal()
    assert animal.location == WorldCell(animal.world, 3, 3)
    animal.step()
    assert animal.location in (
        WorldCell(animal.world, x, y)
        for x in range(2, 5)
        for y in range(2, 5)
        if not x == y == 3
    )


def test_move():
    animal = create_test_animal(3, 3, 2)
    assert animal.location == WorldCell(animal.world, 3, 3)
    animal.move()
    assert animal.location in (
        WorldCell(animal.world, x, y)
        for x in range(1, 6)
        for y in range(1, 6)
    )
