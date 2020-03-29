import tkinter as tk

from animal import Animal
from world import World

grid_squares = {}


def handle_click(animal):
    global grid_squares
    grid_squares[(animal.location.x_pos, animal.location.y_pos)].winfo_children()[0]['bg'] = 'light gray'
    animal.move()
    grid_squares[(animal.location.x_pos, animal.location.y_pos)].winfo_children()[0]['bg'] = 'red'


def create_main_visuals(main_layout, world, animal):
    center_frame = tk.Frame(master=main_layout)
    grid_holder = tk.Frame(master=center_frame)

    for i in range(world.size):
        for j in range(world.size):
            frame = tk.Frame(
                master=grid_holder,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()

            grid_squares[(i, j)] = frame

    grid_holder.pack()

    controls = tk.Frame(master=center_frame)
    controls.pack()
    button = tk.Button(master=controls, text='Click me!', command=lambda: handle_click(animal))
    button.pack()

    center_frame.grid(row=0, column=0)


def create_square_details(main_layout):
    square_details = tk.Frame(master=main_layout)
    square_details_label = tk.Label(master=square_details, text='Details for square')
    square_details_label.pack()
    square_details.grid(row=0, column=1)


def main():
    global grid_squares

    world = World(10)
    animal = Animal(world, 0, 0, 1)

    window = tk.Tk()

    main_layout = tk.Frame(master=window)

    create_main_visuals(main_layout, world, animal)
    create_square_details(main_layout)

    main_layout.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
