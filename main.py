import tkinter as tk

from animal import Animal
from world import World

world = None
square_details = None
entity_tracker = None


class AnimalDescriptorWidget(tk.Frame):
    def __init__(self, master, animal):
        super().__init__(master=master, bg='red')
        self._animal = animal

        self.create_ui()

    def create_ui(self):
        animal_label = tk.Label(master=self, text='Animal')
        animal_label.pack()

        energy_label = tk.Label(master=self, text=f'Energy: {self._animal.energy}')
        energy_label.pack()

        track_button = tk.Button(
            master=self,
            text='Track',
            command=lambda animal=self._animal: set_entity_tracker_details(animal)
        )
        track_button.pack()


class AnimalTrackerWidget(tk.Frame):
    def __init__(self, master, animal):
        super().__init__(master=master, bg='blue')
        self._animal = animal

        self.create_ui()

    def create_ui(self):
        animal_label = tk.Label(master=self, text='Animal')
        animal_label.pack()

        location_label = tk.Label(master=self, text=f'Location: {self._animal.location}')
        location_label.pack()

        speed_label = tk.Label(master=self, text=f'Speed: {self._animal.speed}')
        speed_label.pack()

        energy_label = tk.Label(master=self, text=f'Energy: {self._animal.energy}')
        energy_label.pack()


def create_entity_tracker(main_layout):
    global entity_tracker
    entity_tracker = tk.Frame(master=main_layout)
    entity_tracker_title_label = tk.Label(master=entity_tracker, text='Entity Tracker')
    entity_tracker_title_label.pack()
    entity_tracker.grid(row=0, column=0)


def set_entity_tracker_details(animal):
    global entity_tracker
    for child in entity_tracker.winfo_children():
        if type(child) == AnimalTrackerWidget:
            child.destroy()

    AnimalTrackerWidget(entity_tracker, animal).pack()


def create_map_and_controls(main_layout, grid_size):
    global world

    center_frame = tk.Frame(master=main_layout)
    grid_holder = tk.Frame(master=center_frame)

    for i in range(grid_size):
        for j in range(grid_size):
            frame = tk.Button(
                master=grid_holder,
                command=lambda row=i, col=j: set_details_for_square(row, col),
                width=2,
                height=2
            )
            frame.grid(row=i, column=j)

    grid_holder.grid(row=0, column=0)

    controls = tk.Frame(master=center_frame)
    controls.grid(row=1, column=0)
    button = tk.Button(master=controls, text='Click me!', command=world.do_tick)
    button.pack()

    center_frame.grid(row=0, column=1)


def create_square_details(main_layout):
    global square_details
    square_details = tk.Frame(master=main_layout)

    title_label = tk.Label(master=square_details, text='(x, y)')
    title_label.grid(row=0, column=0)

    animals_label = tk.Label(master=square_details, text='Animals:')
    animals_label.grid(row=1, column=0)

    square_details.pack_propagate(False)
    square_details.grid(row=0, column=2)

    return square_details


def set_details_for_square(row, col):
    global world, square_details

    for child in square_details.winfo_children():
        if type(child) == AnimalDescriptorWidget:
            child.destroy()

    cell = world.get_cell(row, col)
    for index, animal in enumerate(cell.animals):
        animal_widget = AnimalDescriptorWidget(square_details, animal)
        animal_widget.grid(row=index + 2, column=0)


def main():
    global world, details, tracker
    world = World()

    window = tk.Tk()

    main_layout = tk.Frame(master=window)

    create_entity_tracker(main_layout)
    create_map_and_controls(main_layout, 10)
    create_square_details(main_layout)

    main_layout.pack()

    _ = Animal(world, 0, 0, 1)

    window.mainloop()


if __name__ == "__main__":
    main()
