import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples,
        edgecolor='none', s=1)

    # Emphasize first and last points
    plt.scatter(0,0, c='green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors = 'none',
        s = 100)

    plt.axis('Off')

    plt.show()

    keep_running = input("Make another walk (Y/n): ")
    if keep_running.lower() == 'n':
        break
