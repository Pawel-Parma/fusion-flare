import random


def generate_maze(width: int, lenght: int):  # TODO: make better (real generation)
    maze = []

    for i in range(lenght):
        maze.append([])
        for j in range(width):
            if i == 0 or i == lenght - 1:
                maze[i].append("#")

            elif j == 0 or j == width - 1:
                maze[i].append("#")

            else:
                maze[i].append(random.choice(("#", "#", "#", ".", ".", ".", ".")))

    start = random.randint(1, width - 2), random.randint(1, lenght - 2)
    maze[start[0]][start[1]] = "s"
    end = random.randint(1, width - 2), random.randint(1, lenght - 2)
    maze[end[0]][end[1]] = "e"

    make_empty_around(maze, lenght, width, start)
    make_empty_around(maze, lenght, width, end)

    return maze, start, end


def make_empty_around(maze, lenght, width, point):
    x, y = point
    prev = maze[x][y]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < lenght and 0 <= y + j < width:
                maze[x + i][y + j] = "."

    maze[x][y] = prev


class Maze:
    def __init__(self, width: int, length: int, height: int = 1):
        self.new(width, length, height)

    def new(self, width: int, length: int, height: int = 1):
        self.width = width
        self.length = length
        self.height = height
        data = generate_maze(width, length)
        self.maze = data[0]
        self.start = data[1]
        self.end = data[2]

    def __getitem__(self, item):
        return self.maze[item]
