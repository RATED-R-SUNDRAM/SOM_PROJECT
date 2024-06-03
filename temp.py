import matplotlib.pyplot as plt  # Import required dependency: matplotlib for plotting
#from minisom import MiniSom  # Import required dependency: MiniSom library for SOM
import pandas as pd  # Import required dependency: pandas for data manipulation

import numpy as np
import matplotlib.pyplot as plt

def create_grid(m, n):
    # Create an m×n grid with zeros (white background)
    grid = np.zeros((m, n))
    return grid
markers = ['o', 's', 'D']
colors = ['r', 'g', 'b']
def mark_cell(grid, i, j):
    # Place a marker (e.g., "*") in the cell at position (i, j)
    #grid[i, j] = 1  # You can use any non-zero value to represent the marker
    #plt.grid(1+.5, 2+.5, markers[0], markerfacecolor='None',
              #  markeredgecolor=colors[1], markersize=12, markeredgewidth=2)
    pass
def plot_grid(grid):
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap='gray', origin='upper')

    # Draw thicker gridlines (increase linewidth)
    ax.set_xticks(np.arange(-0.5, grid.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, grid.shape[0], 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    plt.grid(1+.5, 2+.5, markers[0], markerfacecolor='None',
                markeredgecolor=colors[1], markersize=12, markeredgewidth=2)

    plt.show()

# Example usage:
m, n = 5, 7  # Set your desired dimensions
my_grid = create_grid(m, n)
mark_cell(my_grid, 2, 3)  # Place a marker in cell at (2, 3)
plot_grid(my_grid)



plt.figure(figsize=(9,9))
#plt.pcolor(som.distance_map().T, cmap='bone_r')  # plotting the distance map as background
#plt.colorbar()

# palce a marker on the winning position for the sample xx
plt.plot

plt.show()