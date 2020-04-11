class Food():
    def __init__(self, world, x_pos, y_pos, nutrition):
        self._nutrition = nutrition

        world.get_cell(x_pos, y_pos).add_food(self)

    @property
    def nutrition(self):
        return self._nutrition
