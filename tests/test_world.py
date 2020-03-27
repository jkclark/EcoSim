from world import World, WorldCell


def create_test_world():
    return World()


class Bunch():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


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


def test_add_and_remove_animal_success():
    world = create_test_world()
    assert world.animals == []

    animal = Bunch(location=Bunch(x_pos=0, y_pos=0))
    world.add_animal(animal)
    assert world.animals == [animal]

    world.remove_animal(animal)
    assert world.animals == []


def test_remove_animal_no_such_animal(capsys):
    world = create_test_world()
    assert world.animals == []

    animal = Bunch(location=Bunch(x_pos=0, y_pos=0))
    world.add_animal(animal)
    assert world.animals == [animal]

    fake_animal = Bunch()
    world.remove_animal(fake_animal)
    assert world.animals == [animal]
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot remove animal from World(grid_size=10).\n'
