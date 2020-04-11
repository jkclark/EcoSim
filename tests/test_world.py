from animal import Animal
from lib.test_helpers import Bunch, create_test_world
from world import WorldCell


def test_size():
    world = create_test_world()
    assert world.size == 10


def test_get_cell_success():
    world = create_test_world()
    cell = world.get_cell(3, 3)
    assert cell == WorldCell(world, 3, 3)


def test_get_cell_invalid_location():
    world = create_test_world()
    cell = world.get_cell(1, -1)
    assert not cell

    cell = world.get_cell(1, 10)
    assert not cell

    cell = world.get_cell(1, "abc")
    assert not cell


def test_add_and_remove_animal():
    world = create_test_world()
    assert world.animals == []

    animal = Animal(world, 0, 0, 1)
    assert world.animals == [animal]
    assert world.get_cell(0, 0).animals == [animal]

    world.remove_animal(animal)
    assert world.animals == []


def test_add_animal_non_animal(capsys):
    world = create_test_world()

    animal = Bunch(location=Bunch(x_pos=0, y_pos=0))
    world.add_animal(animal)
    assert world.animals == []
    # WorldCell.add_animal will also print an error, so just check that World's error is there.
    assert 'Error: Cannot add non-Animal object Bunch to World(size=10).\n' \
        in capsys.readouterr()[0]


def test_remove_animal_no_such_animal(capsys):
    world = create_test_world()
    animal = Animal(world, 0, 0, 1)

    animal_not_present = Bunch()
    world.remove_animal(animal_not_present)
    assert world.animals == [animal]
    assert capsys.readouterr()[0] == 'Error: Cannot remove animal from World(size=10).\n'
