'''This module contains classes which represent the world of the ecosystem.

Ideas:
    - Some spaces should have rocks which make them inacessible to certain animals.
    - Some spaces should have trees which certain animals can interact with.
    - Some spaces should have water which makes the inaccessible to certain animals.
        - Water is also drinkable.

    - Maybe cells should have enter() and exit() functions?
'''


class World(object):

    """Docstring for World. """

    def __init__(self, grid_size=10):
        """TODO: to be defined. """
        self.grid_size = grid_size
        self.grid = {
            (x, y): WorldCell(x, y, self)
            for x in range(grid_size)
            for y in range(grid_size)
        }

    def get_cell(self, x, y):
        try:
            return self.grid[(x, y)]
        except KeyError:
            return None


class WorldCell(object):

    """Docstring for WorldCell. """

    def __init__(self, x_pos, y_pos, grid):
        """TODO: to be defined. """
        self.grid = grid
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def location(self):
        return (self.x_pos, self.y_pos)

    def get_adjacent_cells(self):
        # FIXME: I don't like the 'and' condition here because we check that
        #        condition up to 9 times, when we know it will apply only once.
        return [
            self.grid.get_cell(self.x_pos + x_delta, self.y_pos + y_delta)
            for x_delta in [-1, 0, 1]
            for y_delta in [-1, 0, 1]
            if self.grid.get_cell(self.x_pos + x_delta, self.y_pos + y_delta)
            and not x_delta == y_delta == 0
        ]

    def __repr__(self):
        return f'Cell at ({self.x_pos}, {self.y_pos})'
