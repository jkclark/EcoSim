import tkinter as tk

from world import World


def main():
    world = World(10)

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

    grid_holder.pack()

    controls = tk.Frame(master=window)
    button = tk.Button(master=controls, text='Click me!')
    button.pack()
    controls.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
