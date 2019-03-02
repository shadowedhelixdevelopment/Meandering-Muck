import numpy
from numpy.random import randint as rand
import matplotlib.pyplot as pyplot


def make_maze():
    shape = ((height * 2) + 1, (width * 2) + 1)
    # Build Maze
    maze = numpy.zeros(shape, dtype=int)
    # Fill borders
    maze[0, :] = maze[-1, :] = 1
    maze[:, 0] = maze[:, -1] = 1
    minx = 0
    maxx = (width * 2)
    miny = 0
    maxy = (height * 2)
    maze = maze_section(maze, minx, maxx, miny, maxy)
    return maze


def maze_section(maze, minx, maxx, miny, maxy):
    skip = 0
    # check for 1 and 2 space corridors
    if (maxx - minx) <= (wall + (corr * 2)) or (maxy - miny) <= (wall + (corr * 2)):
        return maze
    # Push wall & corr out of min, but leave it in the max as the max is never picked
    wallx = rand((minx + corr + wall), maxx - wall)
    wally = rand((miny + corr + wall), maxy - wall)
    # set bits to 1 for the walls
    maze[wally, (minx + wall):maxx] = 2
    maze[(miny + wall):maxy, wallx] = 2
    # Make 3 doors at random
    # coin flip to see if a door should be placed, otherwise flag a skip
    if rand(1, 3) == 1:
        print("North")
        maze = door(maze, "x", wallx, miny, wally)  # N
    else:
        skip = 1
    if rand(1, 3) == 1 or skip == 1:
        print("East")
        maze = door(maze, "y", wally, wallx, maxx)  # E
    else:
        skip = 1
    if rand(1, 3) == 1 or skip == 1:
        print("South Door")
        maze = door(maze, "x", wallx, wally, maxy)  # S
    else:
        skip = 1
    if skip == 1:
        print("West")
        maze = door(maze, "y", wally, minx, wallx)  # W

    maze = maze_section(maze, minx, wallx, miny, wally)
    maze = maze_section(maze, wallx, maxx, miny, wally)
    maze = maze_section(maze, minx, wallx, wally, maxy)
    maze = maze_section(maze, wallx, maxx, wally, maxy)
    return maze


def door(maze, axis, wallpoint, mind, maxd):
    door = rand((mind + wall), maxd)
    if axis == "x":
        maze[door, wallpoint] = 0
    else:
        maze[wallpoint, door] = 0
    return maze


width = 5
height = 5
corr = 1
wall = 1

pyplot.figure(figsize=(10, 5))
pyplot.imshow(make_maze(), cmap=pyplot.cm.binary, interpolation=None)
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
