from animal import Animal
from lib.test_helpers import create_test_world
from world import WorldCell


def create_test_animal(x_pos=3, y_pos=3, speed=1):
    world = create_test_world()
    animal = Animal(world, x_pos, y_pos, speed)
    return animal


def test_repr():
    animal = create_test_animal(x_pos=1, y_pos=1)
    assert repr(animal) == 'Animal at (1, 1)'


def test_set_energy_success():
    animal = create_test_animal()
    assert animal.energy == 100

    animal.energy = 50
    assert animal.energy == 50


def test_set_energy_non_int(capsys):
    animal = create_test_animal()
    assert animal.energy == 100

    animal.energy = 50.00
    assert animal.energy == 100
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot set energy to 50.0.\n'

    animal.energy = "fifty"
    assert animal.energy == 100
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot set energy to fifty.\n'


def test_set_energy_negative(capsys):
    animal = create_test_animal()
    assert animal.energy == 100

    animal.energy = -50
    assert animal.energy == 100
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot set energy to -50.\n'


def test_set_energy_greater_than_max(capsys):
    animal = create_test_animal()
    assert animal.energy == 100

    animal.energy = 200
    assert animal.energy == 100
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot set energy to 200.\n'


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


def test_spend_energy_insufficient_energy(capsys):
    animal = create_test_animal()

    @Animal.spend_energy(101)
    def test_func(self):
        pass
    setattr(Animal, 'test_func', test_func)

    assert animal.energy == 100
    animal.test_func()
    assert animal.energy == 100


def test_spend_energy_invalid_value(capsys):
    animal = create_test_animal()

    @Animal.spend_energy("abc")
    def test_func(self):
        pass
    setattr(Animal, 'test_func', test_func)

    assert animal.energy == 100
    animal.test_func()
    assert animal.energy == 100
    out, _ = capsys.readouterr()
    assert out == 'Error: abc is not a valid number.\n'


def test_step_random():
    '''Test stepping to a randomly-chosen location.'''
    animal = create_test_animal()
    assert animal.location == WorldCell(animal.world, 3, 3)

    animal.step()
    assert animal.location in (
        WorldCell(animal.world, x, y)
        for x in range(2, 5)
        for y in range(2, 5)
        if not x == y == 3
    )


def test_step_specific_success():
    '''Test successfully stepping to a specific location.'''
    animal = create_test_animal()
    assert animal.location == WorldCell(animal.world, 3, 3)
    assert animal.energy == 100

    animal.step(new_location=WorldCell(animal.world, 3, 4))
    assert animal.location == WorldCell(animal.world, 3, 4)
    assert animal.energy == 90


def test_step_specific_invalid_location(capsys):
    '''Test attempting to step to an invalid location.'''
    animal = create_test_animal()
    assert animal.location == WorldCell(animal.world, 3, 3)
    assert animal.energy == 100

    animal.step(new_location=WorldCell(animal.world, 5, 5))
    assert animal.location == WorldCell(animal.world, 3, 3)
    assert animal.energy == 100  # No energy should have been spent.
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot move to (5, 5) from (3, 3).\n'
