import random


def generate_maze(width: int, lenght: int, height: int):  # TODO: make better (real generation)
    maze = []
    for x in range(width):
        maze.append([])
        # for y in range(height):
        for z in range(lenght):
            if x == 0 or x == width - 1:
                maze[x].append("#")

            elif z == 0 or z == lenght - 1:
                maze[x].append("#")

            else:
                maze[x].append(random.choice(("#", "#", "#", ".", ".", ".", ".", ".")))

    start = (random.randint(1, width - 2), 0, random.randint(1, lenght - 2))
    maze[start[0]][start[2]] = "s"
    end = (random.randint(1, width - 2), 0, random.randint(1, lenght - 2))
    maze[end[0]][end[2]] = "e"

    make_empty_around(maze, start, lenght, width, height)
    make_empty_around(maze, end, lenght, width, height)

    return maze, start, end


def make_empty_around(maze, point, lenght, width, height):
    x, y, z = point
    prev = maze[x][z]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < width and 0 <= z + j < lenght:
                maze[x + i][z + j] = "."

    maze[x][z] = prev


class Maze:
    def __init__(self, width: int, length: int, height: int = 1):
        self.new(width, length, height)  # Do not generate maze on creation

    def new(self, width: int, length: int, height: int = 1):
        self.width = width
        self.length = length
        self.height = height
        data = generate_maze(width, length, height)
        self.maze = data[0]
        self.start = data[1]
        self.end = data[2]
        self.start_in_map_coords = (self.start[0] * 2 - self.width, 0, self.start[2] * 2 - self.length)
        self.end_in_map_coords = (self.end[0] * 2 - self.width, 0, self.end[2] * 2 - self.length)

    def __getitem__(self, item):
        return self.maze[item]
