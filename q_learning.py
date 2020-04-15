from random import choice

from animal import Animal
from food import Food
from ui import UI
from world import World


class QLearning():
    def __init__(self, world, alpha, gamma):
        self._world = world
        self._alpha = alpha
        self._gamma = gamma

        self._q = {}
        self.initialize_q()

    @property
    def q(self):
        return self._q

    def initialize_q(self):
        self._q = {}
        for r in range(self._world.size):
            for c in range(self._world.size):
                # Create the subdict of possible next moves and their values
                self._q[(r, c)] = {}

                # Initialize all values to 0
                cell = self._world.get_cell(r, c)
                for next_cell in cell.get_adjacent_cells():
                    self._q[(r, c)][(next_cell.x_pos, next_cell.y_pos)] = 0

    def train(self, iterations):
        for i in range(iterations):
            # Choose a random starting position
            start_pos = choice([
                (x, y)
                for x in range(self._world.size) for y in range(self._world.size)
                if self._world.get_cell(x, y).food == []
            ])

            # Choose a random next position
            next_pos = choice(self._world.get_cell(*start_pos).get_adjacent_cells())

            # Measure the reward for moving to this next position
            reward = 0 if next_pos.food == [] else 999

            # Update Q
            self._q[start_pos][(next_pos.x_pos, next_pos.y_pos)] += \
                self._alpha * (
                    reward + self._gamma * max(self._q[(next_pos.x_pos, next_pos.y_pos)].values())
                    - self._q[start_pos][(next_pos.x_pos, next_pos.y_pos)]
                )


def main():
    world = World(size=5)
    animal = Animal(world, 0, 0, 1)
    Food(world, 0, 4, 10)

    q_learning = QLearning(world, 0.75, 0.85)
    q_learning.train(1000)

    animal.q = q_learning.q

    ui = UI(world)
    ui.start()


if __name__ == "__main__":
    main()
