import random
import numpy as np


def generate_maze(width: int, length: int):  # TODO: make better
    maze = np.full((width, length), "#")

    x, y = (2, 2)
    maze[x, y] = "."

    maze[2 * x + 1, 2 * y + 1] = "."

    stack = [(x, y), ]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while len(stack) > 0:
        x, y = stack[-1]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= 2 * nx + 1 < width and 0 <= 2 * ny + 1 < length and maze[2 * nx + 1, 2 * ny + 1] == "#":
                maze[2 * nx + 1, 2 * ny + 1] = "."

                maze[2 * x + dx + 1, 2 * y + dy + 1] = "."
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    for i in range(length):
        if maze[-1, i] == ".":
            maze[-1, i] = "#"
            maze[-2, i] = "."

    for j in range(width):
        if maze[j, -1] == ".":
            maze[j, -1] = "#"
            maze[j, -2] = "."

    maze[2, 2] = "s"
    make_empty_around(maze, (2, 0, 2), length, width)
    maze[width - 3, length - 3] = "e"
    make_empty_around(maze, (width - 3, 0,  length - 3), length, width)

    return maze, (2, 0, 2), (width - 3, 0, length - 3)


def make_empty_around(maze, point, length, width):
    x, y, z = point
    prev = maze[x][z]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < width and 0 <= z + j < length:
                maze[x + i][z + j] = "."

    maze[x][z] = prev


class Maze:
    def __init__(self):
        self.width = 0
        self.length = 0
        self.height = 0

        self.maze = []
        self.start = None
        self.end = None
        self.start_in_map_coords = (0, 0, 0)
        self.end_in_map_coords = (0, 0, 0)

    def new(self, width: int, length: int, height: int = 1):
        self.width = width
        self.length = length
        self.height = height
        data = generate_maze(width, length)
        self.maze = data[0]
        self.start = data[1]
        self.end = data[2]
        self.start_in_map_coords = (self.start[0] * 2 - self.width, 0, self.start[2] * 2 - self.length)
        self.end_in_map_coords = (self.end[0] * 2 - self.width, 0, self.end[2] * 2 - self.length)

    def __getitem__(self, item):
        return self.maze[item]
