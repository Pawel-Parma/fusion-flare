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
    end = random.randint(1, width - 2), random.randint(1, lenght - 2)

    maze[start[1]][start[0]] = "s"
    maze[end[1]][end[0]] = "e"

    maze[lenght // 2 - 1][width // 2] = "."
    maze[lenght // 2 - 1][width // 2 - 1] = "."
    maze[lenght // 2 - 1][width // 2 + 1] = "."
    maze[lenght // 2 + 1][width // 2] = "."
    maze[lenght // 2 + 1][width // 2 - 1] = "."
    maze[lenght // 2 + 1][width // 2 + 1] = "."
    maze[lenght // 2][width // 2] = "."
    maze[lenght // 2][width // 2 - 1] = "."
    maze[lenght // 2][width // 2 + 1] = "."

    return maze, start, end


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
