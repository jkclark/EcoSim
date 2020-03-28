import tkinter as tk

from animal import Animal
from world import World

grid_squares = {}


def handle_click(animal):
    global grid_squares
    grid_squares[(animal.location.x_pos, animal.location.y_pos)].winfo_children()[0]['bg'] = 'light gray'
    animal.move()
    grid_squares[(animal.location.x_pos, animal.location.y_pos)].winfo_children()[0]['bg'] = 'red'


def main():
    global grid_squares

    world = World(10)
    animal = Animal(world, 0, 0, 1)

    window = tk.Tk()

    grid_holder = tk.Frame(master=window)

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

    controls = tk.Frame(master=window)
    button = tk.Button(master=controls, text='Click me!', command=lambda: handle_click(animal))
    button.pack()
    controls.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
