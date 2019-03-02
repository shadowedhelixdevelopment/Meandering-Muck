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
    maze = maze_section(maze, minx, maxx, miny, maxy, 1)
    return maze


def maze_section(maze, minx, maxx, miny, maxy, iteration):
    skip = 0
    # Test to see if there is room for walls
    invalidcols = [(miny + wall), (maxy - wall)]
    for y in range((miny + wall), (maxy - wall)):
        if maze[y, minx] != 1 or maze[y, maxx] != 1:
            if y not in invalidcols:
                invalidcols.append(y)
    invalidrows = [(minx + wall), (maxx - wall)]
    for x in range((minx + wall), (maxx - wall)):
        if maze[miny, x] != 1 or maze[maxy, x] != 1:
            if x not in invalidrows:
                invalidrows.append(x)
    # check for corridors that are too small for a wall due to the 1 space on either side limit and door positioning
    if (maxx - minx) <= len(invalidrows) + wall or (maxy - miny) <= len(invalidcols) + wall:
        return maze
    # Push wall & corr out of min, but leave it in the max as the max is never picked
    wallx = 0
    while wallx == 0 or wallx in invalidrows:
        wallx = rand((minx + corr + wall), maxx - wall)
    wally = 0
    while wally == 0 or wally in invalidcols:
        wally = rand((miny + corr + wall), maxy - wall)
    # set bits to 1 for the walls
    maze[wally, (minx + wall):maxx] = 1
    maze[(miny + wall):maxy, wallx] = 1
    # Make 3 doors at random
    # coin flip to see if a door should be placed, otherwise flag a skip
    if rand(1, 3) == 1:
        print("North")
        maze = door(maze, "x", wallx, miny, wally)  # N
    else:
        skip = 1
    if rand(1, 3) == 1 or skip > 0:
        print("East")
        maze = door(maze, "y", wally, wallx, maxx)  # E
    else:
        skip = 2
    if rand(1, 3) == 1 or skip > 0:
        print("South Door")
        maze = door(maze, "x", wallx, wally, maxy)  # S
    else:
        skip = 3
    if skip > 0:
        print("West")
        maze = door(maze, "y", wally, minx, wallx)  # W
    # Determine where the start and end are
    if iteration == 1:
        if skip == 1:
            if rand(1,3) == 1:
                point = 2
            else:
                point = 3
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), minx] = point
            else:
                maze[miny, rand((minx + 1), wallx)] = point
            if point == 2:
                point = 3
            else:
                point = 2
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), maxx] = point
            else:
                maze[miny, rand((wallx + 1), maxx)] = point
        elif skip == 2:
            if rand(1,3) == 1:
                point = 2
            else:
                point = 3
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), maxx] = point
            else:
                maze[miny, rand((wallx + 1), maxx)] = point
            if point == 2:
                point = 3
            else:
                point = 2
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), maxx] = point
            else:
                maze[maxy, rand((wallx + 1), maxx)] = point
        elif skip == 3:
            if rand(1,3) == 1:
                point = 2
            else:
                point = 3
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), maxx] = point
            else:
                maze[maxy, rand((wallx + 1), maxx)] = point
            if point == 2:
                point = 3
            else:
                point = 2
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), minx] = point
            else:
                maze[maxy, rand((minx + 1), wallx)] = point
        else:
            if rand(1,3) == 1:
                point = 2
            else:
                point = 3
            if rand(1, 3) == 1:
                maze[rand((wally + 1), maxy), minx] = point
            else:
                maze[maxy, rand((minx + 1), wallx)] = point
            if point == 2:
                point = 3
            else:
                point = 2
            if rand(1, 3) == 1:
                maze[rand((miny + 1), wally), minx] = point
            else:
                maze[miny, rand((minx + 1), wallx)] = point
    # Check to see if each chamber needs to be broken into more chambers
    maze = maze_section(maze, minx, wallx, miny, wally, (iteration + 1))
    maze = maze_section(maze, wallx, maxx, miny, wally, (iteration + 1))
    maze = maze_section(maze, minx, wallx, wally, maxy, (iteration + 1))
    maze = maze_section(maze, wallx, maxx, wally, maxy, (iteration + 1))
    return maze


def door(maze, axis, wallpoint, mind, maxd):
    door = rand((mind + wall), maxd)
    if axis == "x":
        maze[door, wallpoint] = 0
    else:
        maze[wallpoint, door] = 0
    return maze


width = 25
height = 25
corr = 1
wall = 1

pyplot.figure(figsize=(10, 5))
pyplot.imshow(make_maze(), cmap=pyplot.cm.binary, interpolation=None)
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
