from random import choice, random


class Animal(object):
    '''A superclass for each animal species.

    Ideas:
        - Be able to get the number of a animals of a certain species in the world
        - Animals should be able to die
        - Animals need to be able to reproduce
    '''

    def __init__(self, world, x_pos, y_pos, speed):
        self._world = world
        self._location = world.get_cell(x_pos, y_pos)

        self._sex = 'M' if random() < 0.5 else 'F'
        self._speed = speed

        self._health = 100
        self._energy = self._max_energy = 100

    @property
    def world(self):
        return self._world

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        self._location = new_location

    @property
    def speed(self):
        return self._speed

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if not type(value) == int or value > self._max_energy or value < 0:
            print('Error: Cannot set energy to {value}.')
        else:
            self._energy = value

    def spend_energy(cost):
        def real_decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    if cost > args[0].energy or cost < 0:
                        return
                except TypeError:
                    print('Error: "Cost" is not a valid number.')
                else:
                    # A truthy return value from func indicates the action was not performed.
                    if not func(args[0], **kwargs):
                        setattr(args[0], 'energy', getattr(args[0], 'energy') - cost)
            return wrapper
        return real_decorator

    @spend_energy(10)
    def step(self, new_location=None):
        '''Step to a specific location, or step in a random direction if no location is provided.'''
        adjacent_cells = self.location.get_adjacent_cells()
        if new_location:
            if new_location in adjacent_cells:
                self.location = new_location
            else:
                return f'Error: Cannot move to {new_location} from {self.location}.'
        else:
            self.location = choice(self.location.get_adjacent_cells())

    def move(self):
        for i in range(self.speed):
            self.step()
