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


def maze_section(maze, minx, maxx, miny, maxy, iteration=0, grid=0):
    wallx = rand(minx, maxx)
    wally = rand(miny, maxy)
    # maze[(minx - minspace), wally] = maze[(maxx + minspace - 1), wally] = 1
    # maze[wallx, (miny - minspace)] = maze[wallx, (maxy + minspace - 1)] = 1
    maze[(minx - minspace):(maxx + minspace), wally] = 1
    maze[wallx, (miny - minspace):(maxy + minspace)] = 1
    if wallx - minspace > minx and wally - minspace > miny:
        maze = maze_section(maze, minx, (wallx - minspace - 1), miny, (wally - minspace), (iteration + 1), 1)
    if wallx + minspace < maxx and wally - minspace > miny:
        maze = maze_section(maze, (wallx + minspace), maxx, miny, (wally - minspace), (iteration + 1), 2)
    if wallx - minspace > minx and wally + minspace < maxy:
        maze = maze_section(maze, minx, (wallx - minspace), (wally + minspace), maxy, (iteration + 1), 3)
    if wallx + minspace < maxx and wally + minspace < maxy:
        maze = maze_section(maze, (wallx + minspace), maxx, (wally + minspace), maxy, (iteration + 1), 4)
    return maze


width = 200
height = 200
minspace = 10

pyplot.figure(figsize=(10, 5))
pyplot.imshow(make_maze(), cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()

