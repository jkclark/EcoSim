from functools import wraps
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

    def __init__(self, world, x_pos, y_pos, speed):
        """TODO: to be defined. """
        self._world = world
        self._location = world.get_cell(x_pos, y_pos)

        self._sex = 'M' if random() < 0.5 else 'F'
        self._speed = speed

        self._hunger = 100
        self._energy = 100

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        self._location = new_location

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value

    def spend_energy(cost):
        def real_decorator(func):
            def wrapper(*args):
                func(args[0])
                setattr(args[0], 'energy', getattr(args[0], 'energy') - cost)
            return wrapper
        return real_decorator

    @spend_energy(10)
    def step(self):
        '''Take a step in a random direction.'''
        self.location = choice(self.location.get_adjacent_cells())

    def move(self):
        for i in range(self.speed):
            self.step()
