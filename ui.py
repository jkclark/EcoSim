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

        self._location_textvar = tk.StringVar()
        self._location_textvar.set('Location: ' + str(animal.location))

        self._speed_textvar = tk.StringVar()
        self._speed_textvar.set('Speed: ' + str(animal.speed))

        self._energy_textvar = tk.StringVar()
        self._energy_textvar.set('Energy: ' + str(animal.energy))

        self.create_ui()

    @property
    def animal(self):
        return self._animal

    def create_ui(self):
        animal_label = tk.Label(master=self, text='Animal')
        animal_label.pack()

        location_label = tk.Label(master=self, textvariable=self._location_textvar)
        location_label.pack()

        speed_label = tk.Label(master=self, textvariable=self._speed_textvar)
        speed_label.pack()

        energy_label = tk.Label(master=self, textvariable=self._energy_textvar)
        energy_label.pack()

    def update_labels(self):
        self._location_textvar.set('Location: ' + str(self._animal.location))
        self._speed_textvar.set('Speed: ' + str(self._animal.speed))
        self._energy_textvar.set('Energy: ' + str(self._animal.energy))


class UI():
    def __init__(self, world):
        self._world = world
        self._window = tk.Tk()

        self._tracker_widget = None
        self._grid_frame = None
        self._detail_location_textvar = tk.StringVar()
        self._detail_location_textvar.set('(x, y)')
        self._selected_location = None

        self._entity_tracker = self.create_entity_tracker()
        self.create_map_and_controls(world.size)
        self.square_details = self.create_square_details()

    def start(self):
        self._window.mainloop()

    def do_world_tick(self):
        self._world.do_tick()

        if self._tracker_widget:
            self._tracker_widget.update_labels()

            row = self._tracker_widget.animal.location.x_pos
            col = self._tracker_widget.animal.location.y_pos

            for r in range(self._world.size):
                for c in range(self._world.size):
                    if self._grid_frame.grid_slaves(r, c):
                        btn = self._grid_frame.grid_slaves(r, c)[0]
                        if r == row and c == col:
                            btn.config(bg='blue')
                        else:
                            btn.config(bg='light gray')

        if self._selected_location:
            self.set_details_for_square(*self._selected_location)

    def create_entity_tracker(self):
        entity_tracker = tk.Frame(master=self._window)

        entity_tracker_title_label = tk.Label(master=entity_tracker, text='Entity Tracker')
        entity_tracker_title_label.pack()

        entity_tracker.grid(row=0, column=0)
        return entity_tracker

    def create_map_and_controls(self, grid_size):
        center_frame = tk.Frame(master=self._window)
        self._grid_frame = grid_holder = tk.Frame(master=center_frame)

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
        button = tk.Button(master=controls, text='Click me!', command=self.do_world_tick)
        button.pack()

        center_frame.grid(row=0, column=1)

    def create_square_details(self):
        square_details = tk.Frame(master=self._window)

        title_label = tk.Label(master=square_details, textvariable=self._detail_location_textvar)
        title_label.grid(row=0, column=0)

        animals_label = tk.Label(master=square_details, text='Animals:')
        animals_label.grid(row=1, column=0)

        square_details.pack_propagate(False)
        square_details.grid(row=0, column=2)

        return square_details

    def set_entity_tracker_details(self, animal):
        for child in self._entity_tracker.winfo_children():
            if type(child) == AnimalTrackerWidget:
                child.destroy()

        self._tracker_widget = AnimalTrackerWidget(self._entity_tracker, animal)
        self._tracker_widget.pack()

    def set_details_for_square(self, row, col):
        self._selected_location = (row, col)

        self._detail_location_textvar.set(f'({row}, {col})')

        # FIXME: For some reason, setting the background color here and also in
        #        do_world_tick doesn't work. Need to investigate what actually happens
        #        when you call btn.config(bg='').
        # Color in only this button on the grid
        #  for r in range(self._world.size):
        #       for c in range(self._world.size):
        #           if self._grid_frame.grid_slaves(r, c):
        #              btn = self._grid_frame.grid_slaves(r, c)[0]
        #              if r == row and c == col:
        #                  btn.config(bg='red')
        #              else:
        #                  btn.config(bg='light gray')

        for child in self.square_details.winfo_children():
            if type(child) == AnimalDescriptorWidget:
                child.destroy()

        cell = self._world.get_cell(row, col)
        for index, animal in enumerate(cell.animals):
            animal_widget = AnimalDescriptorWidget(self, animal)
            animal_widget.grid(row=index + 2, column=0)
