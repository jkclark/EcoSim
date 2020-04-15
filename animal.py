from random import choice


class Animal(object):
    '''A superclass for each animal species.

    Ideas:
        - Be able to get the number of a animals of a certain species in the world
        - Animals should be able to die
        - Animals need to be able to reproduce
    '''

    def __init__(self, world, x_pos, y_pos, speed):
        # Location
        # TODO: What happens if (x_pos, y_pos) isn't a valid location in world?
        self._world = world
        self._location = world.get_cell(x_pos, y_pos)
        world.add_animal(self)

        self._speed = speed

        self._energy = self._max_energy = 100

        self.q = {}

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
    def speed(self):
        return self._speed

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        # TODO: Allow values greater than self._max_energy to be passed in.
        #       The result should be the animal's energy being set to self._max_energy
        if not isinstance(value, int) or value > self._max_energy or value < 0:
            print(f'Error: Cannot set energy to {value}.')
        else:
            self._energy = value

    def spend_energy(cost):
        def real_decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    if cost > args[0].energy or cost < 0:
                        return
                except TypeError:
                    print(f'Error: {cost} is not a valid number.')
                else:
                    # A truthy return value from func indicates the action was not performed.
                    func_return_value = func(args[0], **kwargs)
                    if not func_return_value:
                        setattr(args[0], 'energy', getattr(args[0], 'energy') - cost)
                    else:
                        print(func_return_value)
            return wrapper
        return real_decorator

    def do_turn(self):
        # HACK: This is not an elegant way to call the q_step function.
        #       Maybe we can give Animal a 'mode' attribute which controls this.
        if self.q:
            self.q_step()
        else:
            self.step()

    @spend_energy(10)
    def step(self, new_location=None):
        '''Step to a specific location, or step in a random direction if no location is provided.'''
        # TODO: I don't think this updates WorldCell.animals
        adjacent_cells = self.location.get_adjacent_cells()
        if new_location:
            if new_location in adjacent_cells:
                self.location = new_location
            else:
                return f'Error: Cannot move to {new_location} from {self.location}.'
        else:
            self.location = choice(self.location.get_adjacent_cells())

    def q_step(self):
        next_moves_to_values = self.q[(self.location.x_pos, self.location.y_pos)]
        new_location = max(next_moves_to_values, key=next_moves_to_values.get)
        self.location = self.world.get_cell(*new_location)

    def eat(self, food):
        if food not in self.location.food:
            print(f'Error: Animal at {self.location} cannot eat food which is not at its location.')
        else:
            self.energy += food.nutrition
            self.location.remove_food(food)
            # NOTE: Is there any real benefit to calling `del food` here?
