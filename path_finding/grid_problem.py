#!env python2
from random import randint, shuffle
from time import sleep
from copy import copy,deepcopy
from pprint import pprint
from termcolor import colored, cprint
from math import sqrt
import sys

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
            child.h = \
                ((child.position[0] - end_node.position[0]) ** 2) + \
                ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            path = [ x.position for x in open_list ]
            print("\033[0;0H")
            print_grid(maze, path)
            #sleep(1/60.0)


def size_to_xy(size):
    coords = size.split("x")
    x = int(coords[0])
    y = int(coords[1])
    return x,y

def make_grid(size):
    x, y = size_to_xy(size)
    row = ['']*y
    row = [ '' for a in range(0, y) ]
    #grid = [ row ]*x
    grid = [ deepcopy(row) for b in range(0, x) ]
    return grid

def rando_coords(x, y):
    rx = randint(0, x-1)
    ry = rx
    while rx == ry:
        ry = randint(0, y-1)
    return rx, ry

def n_spots(count, size):
    x, y = size_to_xy(size)
    spots = []
    while len(spots) < count:
        R = rando_coords(x, y)
        if not x in spots:
            #print(z)
            spots.append(R)
    return spots

def mod_grid(grid, start, goal, spot):
    if spot != start or spot != goal:
        mygrid = deepcopy(grid)
        x = spot[0]
        y = spot[1]
        mygrid[x][y] = "#"
        return mygrid

def mark_some(grid, start, goal, spots):
    grout = deepcopy(grid)
    for spot in spots:
        #print(spot)
        grout = mod_grid(grout, start, goal, spot)
    if grout:
        return grout

def highlight(message):
    return colored(message, 'green', attrs=['reverse'])

def distance_from_target(pos, target):
    # a^2 + b^2 = c^2
    # x^2 + y^2 = z^2
    # z2 - z1 = distance
    dx = (target[1] - pos[1])**2
    dy = (target[0] - pos[0])**2
    dz = sqrt(dx + dy)
    return dz

def check_free(grid, pos):
    free = []
    #print("position: {}".format(pos))
    y = pos[0]
    x = pos[1]
    # eg.   grid[ y [ x ... ]]
    if y > 0:                        #  up
        if not grid[y-1][x]:
            free.append( (y-1,x) )

    if y > 0 and x < len(grid[0])-1: # diagonal up-right
        if not grid[y-1][x+1]:
            free.append( (y-1,x+1) )

    if y > 0 and x > 0:              # diagonal up-left
        if not grid[y-1][x-1]:
            free.append( (y-1,x-1) )

    if y < len(grid)-1:              #  down
        if not grid[y+1][x]:
            free.append( (y+1,x) )

    if y < len(grid)-1 and x < len(grid[0])-1:  #  diagonal down-right
        if not grid[y+1][x+1]:
            free.append( (y+1,x+1) )

    if y < len(grid)-1 and x > 0:  #  diagonal down-left
        if not grid[y+1][x-1]:
            free.append( (y+1,x-1) )

    if x > 0:                        # left
        if not grid[y][x-1]:
            free.append( (y,x-1) )

    if x < len(grid[0])-1:           # right
        if not grid[y][x+1]:
            free.append( (y,x+1) )

    return free


def triangle_cost(start, end, pos):
    f = distance_from_target(pos, start) + distance_from_target(pos, end)
    return f


def distance_vector(grid, routes):
    # takes a list of route dicts
    # returns the coords of route vector with lowest weight
    cost = (2.0**63)-1  # go big or go home eq. 9.223372036854776e+18
    picked = ""
    for route in routes:
        pos = route['pos']
        start = route['start']
        end = route['target']
        d = triangle_cost(start, end, pos)
        #print("evaluating {} cost: {}".format(pos, d))
        if d < cost:
            cost = d
            picked = route['pos']
    return picked


def shortest_path_first(grid, start, end, pos, path=[]):
    path.append(pos)
    routes = []
    for node in check_free(grid, pos):
        if node not in path:
            if node == end:
                path.append(node)
                #print("WINNING: {}".format(path))
                return path
            else:
                second_degree_free = check_free(grid, node)
                if len(second_degree_free) > 0:
                    route = { 'pos': node, 'start': start, 'target': end }
                    routes.append(route)
    if len(routes) > 0:
        #pprint(routes)
        direction = distance_vector(grid, routes)
        if direction:
            print("direction: {}".format(direction))
            return shortest_path_first(grid, start, end, direction, path=path)


# GRID Printer
# Calls route picker for path highlighting
def print_grid(grid, path):
    if not path:
        path = []
    out = ""
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column:
                if (i, j) in path:
                    out += highlight("#")
                else:
                    out += "#"
            else:
                if (i,j) in path:
                    out += highlight(" ")
                else:
                    out += " "
        out += "\n"
    cprint(out)



if __name__ == '__main__':
    # parameters
    size = sys.argv[1]  # so you can say "20x30" on the command line
    if not size:
        size = "20x60"

    pct = int(sys.argv[2]) / 100.0
    if not pct:
        pct = 0.19

    # setup start, end
    xy = size_to_xy(size)
    bad = (xy[0]*xy[1])*pct
    start = (0, 0) # center
    end = (xy[0]-1, xy[1]-1)

    # make and mark
    board = make_grid(size)
    bad_spots = n_spots(bad, size)
    #bad_spots = [ (1,6), (2,5), (3,4), (4,3)]
    board = mark_some(board, start, end, bad_spots )

    # pathfinding
    print("start: {} end: {}".format(start, end))
    path = astar(board, start, end)
    print("steps: {}".format(len(path)))
    route = [end, start]
    if type(path) == type(list()):
        route.extend(path)
    #print_grid(board, route)
