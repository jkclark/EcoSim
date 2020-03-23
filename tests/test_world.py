from world import World, WorldCell


def create_test_world():
    return World()


def test_get_cell():
    world = create_test_world()
    cell = world.get_cell(3, 3)
    assert cell == WorldCell(world, 3, 3)
