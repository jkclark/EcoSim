from world import World, WorldCell


def create_test_world():
    return World()


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
