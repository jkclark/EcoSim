
from random import choice, random


class Animal(object):
    '''A superclass for each animal species.

    Ideas:
        - Be able to get the number of a animals of a certain species in the world
        - Animals should have hunger/thirst and health
        - Animals should be able to die
        - Animals can have different speeds which determine how fast they move through the world
        - Animals need to be able to reproduce
        - Actions performed by animals (moving, reproducing, fighting, etc) can have costs
            - Maybe this is a good use case for a decorator?
    '''

    def __init__(self, grid, x_pos, y_pos, speed):
        """TODO: to be defined. """
        self.grid = grid
        self.location = grid.get_cell(x_pos, y_pos)

        self.sex = 'M' if random() < 0.5 else 'F'
        self.speed = speed

    def step(self):
        '''Take a step in a random direction.'''
        self.location = choice(self.location.get_adjacent_cells())
