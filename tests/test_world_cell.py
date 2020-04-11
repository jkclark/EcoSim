from animal import Animal
from food import Food
from lib.test_helpers import Bunch, create_test_world


def test_repr():
    cell = create_test_world().get_cell(3, 3)
    assert repr(cell) == 'WorldCell at (3, 3)'


def test_add_and_remove_animal():
    cell = create_test_world().get_cell(0, 0)
    assert cell.animals == []

    animal = Animal(cell.world, 0, 0, 1)
    assert cell.animals == [animal]

    cell.remove_animal(animal)
    assert cell.animals == []


def test_remove_animal_no_such_animal(capsys):
    cell = create_test_world().get_cell(0, 0)
    animal = Animal(cell.world, 0, 0, 1)

    animal_not_present = Bunch()
    cell.remove_animal(animal_not_present)
    assert cell.animals == [animal]
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot remove animal from (0, 0).\n'


def test_add_and_remove_food():
    world = create_test_world()
    food_cell = world.get_cell(0, 0)
    assert food_cell.food == []

    food = Food(world, 0, 0, 10)
    assert food_cell.food == [food]

    food_cell.remove_food(food)
    assert food_cell.food == []


def test_add_food_non_food(capsys):
    world = create_test_world()
    food_cell = world.get_cell(0, 0)

    non_food = Bunch(nutrition=10)
    food_cell.add_food(non_food)
    assert food_cell.food == []
    assert capsys.readouterr()[0] == 'Error: Cannot add non-Food object Bunch to (0, 0).\n'


def test_remove_food_no_such_food(capsys):
    world = create_test_world()
    food_cell = world.get_cell(0, 0)
    food = Food(world, 0, 0, 10)

    food_not_present = Bunch()
    world.get_cell(0, 0).remove_food(food_not_present)
    assert food_cell.food == [food]
    assert capsys.readouterr()[0] == 'Error: Cannot remove food from (0, 0).\n'
