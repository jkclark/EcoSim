from food import Food
from lib.test_helpers import create_test_world


def test_init():
    '''Test that creating a Food object adds it to its location's food list.'''
    # TODO: I think at this point create_test_world would benefit from a fixture,
    #       as would create_test_animal.
    world = create_test_world()
    food = Food(world, 0, 0, 10)
    assert world.get_cell(0, 0).food == [food]
