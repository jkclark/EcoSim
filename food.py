class Food():
    def __init__(self, world, x_pos, y_pos, nutrition):
        self._world = world
        self._x_pox = x_pos
        self._y_pos = y_pos
        self.nutrition = nutrition

        world.get_cell(x_pos, y_pos)
