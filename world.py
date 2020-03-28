'''This module contains classes which represent the world of the ecosystem.

Ideas:
    - Some spaces should have rocks which make them inacessible to certain animals.
    - Some spaces should have trees which certain animals can interact with.
    - Some spaces should have water which makes the inaccessible to certain animals.
        - Water is also drinkable.
    - Maybe cells should have enter() and exit() functions?
'''


class World(object):
    def __init__(self, grid_size=10):
        self._grid_size = grid_size
        self._grid = {
            (x, y): WorldCell(self, x, y)
            for x in range(grid_size)
            for y in range(grid_size)
        }

        self._animals = []

    def __repr__(self):
        return f'World(grid_size={self._grid_size})'

    def get_cell(self, x, y):
        try:
            return self._grid[(x, y)]
        except KeyError:
            return None

    @property
    def animals(self):
        return self._animals

    def add_animal(self, animal):
        self._animals.append(animal)

        # Add the animal to its current WorldCell too
        self.get_cell(animal.location.x_pos, animal.location.y_pos).add_animal(animal)

    def remove_animal(self, animal):
        try:
            self._animals.remove(animal)
        except ValueError:
            print(f'Error: Cannot remove animal from {self}.')


class WorldCell(object):
    def __init__(self, world, x_pos, y_pos):
        self._world = world
        self._x_pos = x_pos
        self._y_pos = y_pos

        self._animals = []

    def __eq__(self, other):
        if (
            self._world == other.world
            and self._x_pos == other.x_pos
            and self._y_pos == other.y_pos
        ):
            return True
        return False

    def __repr__(self):
        return f'WorldCell at ({self._x_pos}, {self._y_pos})'

    def __str__(self):
        return f'({self._x_pos}, {self._y_pos})'

    @property
    def world(self):
        return self._world

    @property
    def x_pos(self):
        return self._x_pos

    @property
    def y_pos(self):
        return self._y_pos

    @property
    def animals(self):
        return self._animals

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        try:
            self._animals.remove(animal)
        except ValueError:
            print(f'Error: Cannot remove animal from {self}.')

    def get_adjacent_cells(self):
        # FIXME: I don't like the 'and' condition here because we check that
        #        condition up to 9 times, when we know it will apply only once.
        return [
            self._world.get_cell(self.x_pos + x_delta, self.y_pos + y_delta)
            for x_delta in [-1, 0, 1]
            for y_delta in [-1, 0, 1]
            if self._world.get_cell(self.x_pos + x_delta, self.y_pos + y_delta)
            and not x_delta == y_delta == 0
        ]
