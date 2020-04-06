from animal import Animal
from ui import UI
from world import World


def main():
    world = World()
    Animal(world, 0, 0, 1)
    ui = UI(world)
    ui.start()


if __name__ == "__main__":
    main()
