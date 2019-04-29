#!env python2
from random import randint, shuffle
from time import sleep
from copy import copy,deepcopy
from pprint import pprint
from termcolor import colored, cprint
from math import sqrt
import sys
import os


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
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
        print(u"\033[{};{}H\u001b[41m ".format(current_node.position[0], current_node.position[1]))
        sleep(1/120.0)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        # this is the diagonal version
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # diagonal ajacent
        #for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # 4 directions only

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]]:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            # modified heuristic weight formula, picks more lateral movent
            child.h = \
                ((end_node.position[0] - child.position[0]) ** 2) + \
                ((end_node.position[1] - child.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            print(u"\033[{};{}H\u001b[43m ".format(child.position[0], child.position[1]))
            path = [ x.position for x in open_list ]

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

def make_grid(size):
    x, y = size_to_xy(size)
    row = ['']*y
    row = [ '' for a in range(0, y) ]
    grid = [ deepcopy(row) for b in range(0, x) ]
    return grid

def rando_coords(x, y):
    rx = randint(2, x-1)
    ry = randint(1, y-1)
    return rx, ry

def n_spots(count, size):
    x, y = size_to_xy(size)
    spots = []
    while len(spots) < count:
        R = rando_coords(x, y)
        if not x in spots:
            spots.append(R)
    return spots

def mod_grid(grid, start, goal, spot):
    avoid = [ start, goal ]
    if spot not in avoid:
        mygrid = deepcopy(grid)
        x = spot[0]
        y = spot[1]
        mygrid[x][y] = "#"
        return mygrid

def efficient_marks(grid, start, stop, spots):
    grout = deepcopy(grid)
    size = len(grid) * len(grid[0])
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            roll = randint(0, 100)
            pct = size * int(spots)
            if roll < pct:
                grid[i][j] = "#"
    return grout

def mark_some(grid, start, goal, spots):
    grout = deepcopy(grid)
    for spot in spots:
        grout = mod_grid(grout, start, goal, spot)
    if grout:
        return grout

def load_maze(file):
    with open(file) as f:
        board = [ c for c in f.read().split('\n') ]
        start = []
        end = []
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if i == 0 and not j:
                    start = [i, j]
                if i == len(board) and not j:
                    end = [i, j]
    return board, start, end

if __name__ == '__main__':
    if len(sys.argv) > 1:
        board, start, end = load_maze(sys.argv[1])
    else:
        board, start, end = []
        exit
    # pathfinding
    print_grid(board, [])
    path = astar(board, start, end)
    print(u'\033[{};{}H\u001b[0m'.format(end[1], 0))
    print("start: {} end: {}".format(start, end))
    print("Steps taken: {}".format(len(path)))
