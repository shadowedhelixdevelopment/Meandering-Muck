import numpy
from numpy.random import randint as rand
import matplotlib.pyplot as pyplot


def make_maze():
    shape = ((height * 2) + 1, (width * 2) + 1)
    # Build Maze
    maze = numpy.zeros(shape, dtype=bool)
    # Fill borders
    maze[0, :] = maze[-1, :] = 1
    maze[:, 0] = maze[:, -1] = 1
    minx = minspace + 1
    maxx = ((width * 2) + 1) - minspace
    miny = minspace + 1
    maxy = ((height * 2) + 1) - minspace
    maze = maze_section(maze, minx, maxx, miny, maxy)
    return maze


def maze_section(maze, minx, maxx, miny, maxy):
    skip = 0
    # if match, set wall, otherwise make it random
    if minx == maxx:
        wallx = minx
    else:
        wallx = rand(minx, maxx)
    if miny == maxy:
        wally = miny
    else:
        wally = rand(miny, maxy)
    # set bits to 1 for the walls
    maze[wally, (minx - minspace):(maxx + minspace)] = 1
    maze[(miny - minspace):(maxy + minspace), wallx] = 1
    # Make 3 doors at random
    # coin flip to see if a door should be placed, otherwise flag a skip
    if rand(1, 3) == 1:
        maze = door(maze, minx, wallx, wally, "y")  # N
        print("North Door Made")
    else:
        skip = 1
    if rand(1, 3) == 1 or skip == 1:
        maze = door(maze, wally, maxy, wallx, "x")  # E
        print("East Door Made")
    else:
        skip = 1
    if rand(1, 3) == 1 or skip == 1:
        maze = door(maze, wallx, maxx, wally, "y")  # S
        print("South Door Made")
    else:
        skip = 1
    if skip == 1:
        maze = door(maze, miny, wally, wallx, "x")  # W
        print("West Door Made")

    if wallx - minspace > minx and wally - minspace > miny:
        maze = maze_section(maze, minx, (wallx - minspace - 1), miny, (wally - minspace))
    if wallx + minspace < maxx and wally - minspace > miny:
        maze = maze_section(maze, (wallx + minspace), maxx, miny, (wally - minspace))
    if wallx - minspace > minx and wally + minspace < maxy:
        maze = maze_section(maze, minx, (wallx - minspace), (wally + minspace), maxy)
    if wallx + minspace < maxx and wally + minspace < maxy:
        maze = maze_section(maze, (wallx + minspace), maxx, (wally + minspace), maxy)
    return maze


def door(maze, mind, maxd, nondoor, dooraxis):
    if (maxd - mind) <= doorwidth:
        doormin = mind
        doormax = maxd
    else:
        doormin = rand(mind, (maxd - doorwidth))
        doormax = (doormin + doorwidth)
    print(dooraxis, doormin, doormax, nondoor)
    if dooraxis == "x":
        maze[nondoor, round(doormin):round(doormax)] = 0
    else:
        maze[round(doormin):round(doormax), nondoor] = 0
    return maze


width = 15
height = 15
minspace = 2
doorwidth = 1 # round((minspace / 2), 0)

pyplot.figure(figsize=(10, 5))
pyplot.imshow(make_maze(), cmap=pyplot.cm.binary, interpolation=None)
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
