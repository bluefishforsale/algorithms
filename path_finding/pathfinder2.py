#!env python2
from random import random, randint
from time import sleep
from copy import copy,deepcopy
from pprint import pprint
from termcolor import colored, cprint
from math import sqrt
import sys
import os

counter = 0

class Memoize:
    """Remember things for me"""

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
	    self.memo[args] = self.fn(*args)
        return self.memo[args]

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, dead=None):
        self.parent = parent
        self.position = position
        self.dead = dead

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end, rpath={}):
    global counter
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        print(u"\033[{};{}H\u001b[{}m \u001b[0m".format(current_node.position[0], current_node.position[1], 41))  # red
        sleep(1/1440.0)

        # Found the goal and Return path
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current = current_node.parent
                return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]: # diagonal ajacent
        #for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # 4 directions only
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure nodes is within grid range
            if node_position[0] > (len(maze) - 1) \
                or node_position[0] < 0 \
                or node_position[1] > (len(maze[0]) -1) \
                or node_position[1] < 0:
                continue

            # Make sure node is empty
            if maze[node_position[0]][node_position[1]]:
                continue

            # No failures? ok, create the child
            new_node = Node(current_node, node_position)

            # have we been here before?
            if new_node in closed_list:
                continue

            # New node becomes a child!
            children.append(new_node)
            closed_list.append(current_node)

        # Loop through children
        for child in children:
            counter += 1

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    child.dead = True
                    continue

            # Create the f, g, and h values
            # g = distance from start
            # h = a heuristic, end - start**2
            # f = the factor we compare in the end
            child.g = current_node.g + 1
            child.h = \
                ( (end_node.position[0] - child.position[0]) **2) + \
                ( (end_node.position[1] - child.position[1]) **2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            print(u"\033[{};{}H\u001b[{}m \u001b[0m".format(child.position[0], child.position[1], 43  )) # yellow


# GRID Printer
# Calls route picker for path highlighting
def print_grid(grid, path):
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column:  # there's a thing in this spot
                print('\033[{};{}H#'.format(i, j))
            else:  # no thing in this spot
                print('\033[{};{}H '.format(i, j))

def size_to_xy(size):
    coords = size.split("x")
    x = int(coords[0])
    y = int(coords[1])
    return x,y

def make_grid(size, start, end, pct):
    x, y = size_to_xy(size)
    row = ['']*y
    row = [ '' for a in range(0, y) ]
    grid = [ deepcopy(row) for b in range(0, x) ]
    grid = efficient_marks(grid, start, end, pct)
    return grid

def efficient_marks(grid, start, end, pct):
    grout = deepcopy(grid)
    def pct_chance():
        if random() < (pct/100.0):
            return True
        else:
            return False
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if pct_chance():
                grout[i][j] = "#"
            else:
                grout[i][j] = ""
    # make sure we have entrance and exit holes
    grout[start[0]][start[1]] = ""
    grout[end[0]][end[1]] = ""
    return grout

def mark_some(grid, start, goal, spots):
    grout = deepcopy(grid)
    for spot in spots:
        grout = mod_grid(grout, start, goal, spot)
    if grout:
        return grout


if __name__ == '__main__':
    # parameters

    rows, columns = os.popen('stty size', 'r').read().split()
    size="{}x{}".format(int(rows), columns)

    if len(sys.argv) > 1:
        pct_bad = int(sys.argv[1])
    else:
        pct_bad = 25.0

    # setup start, end
    xy = size_to_xy(size)
    bad = (xy[0] * xy[1]) * pct_bad/100.0
    start = (0, 0) # center
    end = (xy[0]-1, xy[1]-1)

    # make and mark
    board = make_grid(size, start, end, pct_bad)

    # pathfinding
    print_grid(board, [])
    path = astar(board, start, end)
    #path = astar(board, end, start)
    print(u'\033[{};{}H\u001b[0m'.format(end[1], 0))
    print(u"Start: {} end: {}, bad: {}".format(start, end, bad))
    print(u"Path lenth: {}".format(len(path)))
    print(u"Steps taken: {}".format(counter))
