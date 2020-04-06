import tkinter as tk


class AnimalDescriptorWidget(tk.Frame):
    def __init__(self, ui, animal):
        super().__init__(master=ui.square_details, bg='red')
        self.ui = ui
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
            command=lambda animal=self._animal: self.ui.set_entity_tracker_details(animal)
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


class UI():
    def __init__(self, world):
        self._world = world
        self._window = tk.Tk()

        self._entity_tracker = self.create_entity_tracker()
        self.create_map_and_controls(world.size)
        self.square_details = self.create_square_details()

    def start(self):
        self._window.mainloop()

    def create_entity_tracker(self):
        entity_tracker = tk.Frame(master=self._window)

        entity_tracker_title_label = tk.Label(master=entity_tracker, text='Entity Tracker')
        entity_tracker_title_label.pack()

        entity_tracker.grid(row=0, column=0)
        return entity_tracker

    def create_map_and_controls(self, grid_size):
        center_frame = tk.Frame(master=self._window)
        grid_holder = tk.Frame(master=center_frame)

        for i in range(grid_size):
            for j in range(grid_size):
                frame = tk.Button(
                    master=grid_holder,
                    command=lambda row=i, col=j: self.set_details_for_square(row, col),
                    width=2,
                    height=2
                )
                frame.grid(row=i, column=j)

        grid_holder.grid(row=0, column=0)

        controls = tk.Frame(master=center_frame)
        controls.grid(row=1, column=0)
        button = tk.Button(master=controls, text='Click me!', command=self._world.do_tick)
        button.pack()

        center_frame.grid(row=0, column=1)

    def set_details_for_square(self, row, col):
        for child in self.square_details.winfo_children():
            if type(child) == AnimalDescriptorWidget:
                child.destroy()

        cell = self._world.get_cell(row, col)
        for index, animal in enumerate(cell.animals):
            animal_widget = AnimalDescriptorWidget(self, animal)
            animal_widget.grid(row=index + 2, column=0)

    def create_square_details(self):
        square_details = tk.Frame(master=self._window)

        title_label = tk.Label(master=square_details, text='(x, y)')
        title_label.grid(row=0, column=0)

        animals_label = tk.Label(master=square_details, text='Animals:')
        animals_label.grid(row=1, column=0)

        square_details.pack_propagate(False)
        square_details.grid(row=0, column=2)

        return square_details

    def set_entity_tracker_details(self, animal):
        global entity_tracker
        for child in self._entity_tracker.winfo_children():
            if type(child) == AnimalTrackerWidget:
                child.destroy()

        AnimalTrackerWidget(self._entity_tracker, animal).pack()
