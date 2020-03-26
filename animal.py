from random import choice, choices


class Animal(object):
    '''A superclass for each animal species.

    Ideas:
        - Be able to get the number of a animals of a certain species in the world
        - Animals should be able to die
        - Animals need to be able to reproduce
    '''

    def __init__(self, world, x_pos, y_pos, speed):
        # Location
        self._world = world
        self._location = world.get_cell(x_pos, y_pos)
        world.add_animal(self)

        self._speed = speed

        self._energy = self._max_energy = 100

    def __repr__(self):
        return f'Animal at {self._location}'

    @property
    def world(self):
        return self._world

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        self._location.remove_animal(self)
        new_location.add_animal(self)
        self._location = new_location

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

    def do_turn(self):
        CHANCE_DO_NOTHING = 0
        CHANCE_MOVE = 1
        actions = ['pass', 'move']
        action = choices(actions, weights=[CHANCE_DO_NOTHING, CHANCE_MOVE], k=1)[0]
        if action == 'pass':
            pass
        if action == 'move':
            self.move()

    def move(self):
        for i in range(self._speed):
            self.step()

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
