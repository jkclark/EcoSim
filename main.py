from world import World

grid = World(10)
print(grid.get_cell(1, 0).get_adjacent_cells())
