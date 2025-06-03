import matplotlib.pyplot as plt
import numpy as np # Often useful for numerical operations

def myDrawSubPlot(ax, data, titolo, labelOrdinate): # Changed plt to ax
    ax.plot(data)
    ax.set_title(titolo) # Use set_title for Axes objects
    ax.set_xlabel("Valori") # Use set_xlabel for Axes objects
    ax.set_ylabel(labelOrdinate) # Use set_ylabel for Axes objects

    # Ensure tick locations are a proper list/array
    ax.set_xticks(list(range(len(data)))) # Set ticks based on the length of the data

    ax.autoscale(True, "both")
    ax.grid(True) # It's good practice to explicitly pass True

figure, subplots = plt.subplots(2, figsize=(12, 6), dpi=100)

squares = [i**2 for i in range(5)]
# Corrected cubes to be a flat list
cubes = [i**3 for i in range(5)]

# Pass the individual subplot axes objects
myDrawSubPlot(subplots[0], squares, "Quadrati del cazzo", "Quadrati")
myDrawSubPlot(subplots[1], cubes, "Cubi del cazzo", "Cubi")

# Adjust layout to prevent titles/labels from overlapping
figure.tight_layout()

plt.show()
