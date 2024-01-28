import random


def generate_maze(width: int, lenght: int):
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

    return maze

