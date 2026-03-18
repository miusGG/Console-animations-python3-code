import math
import time
import os

WIDTH = 80
HEIGHT = 40
SCALE = 30
SPEED = 0.05

POINT_CHAR = "0"
LINE_CHAR = "."


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


points = [
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


def rotate(x, y, z, angle_x, angle_y, angle_z):
    rad = angle_x
    ny = y * math.cos(rad) - z * math.sin(rad)
    nz = y * math.sin(rad) + z * math.cos(rad)
    y, z = ny, nz

    rad = angle_y
    nx = x * math.cos(rad) + z * math.sin(rad)
    nz = -x * math.sin(rad) + z * math.cos(rad)
    x, z = nx, nz

    rad = angle_z
    nx = x * math.cos(rad) - y * math.sin(rad)
    ny = x * math.sin(rad) + y * math.cos(rad)
    x, y = nx, ny

    return x, y, z


angle = 0
print("\033[2J")

try:
    while True:
        grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
        projected_points = []

        for p in points:
            rx, ry, rz = rotate(p[0], p[1], p[2], angle, angle * 0.5, angle * 0.3)

            z_depth = 4
            factor = SCALE / (rz + z_depth)

            x_2d = int(rx * factor * 2) + WIDTH // 2
            y_2d = int(ry * factor) + HEIGHT // 2

            projected_points.append((x_2d, y_2d))

        for edge in edges:
            p1 = projected_points[edge[0]]
            p2 = projected_points[edge[1]]

            steps = 15
            for i in range(steps):
                t = i / steps
                curr_x = int(p1[0] * (1 - t) + p2[0] * t)
                curr_y = int(p1[1] * (1 - t) + p2[1] * t)

                if 0 <= curr_x < WIDTH and 0 <= curr_y < HEIGHT:
                    grid[curr_y][curr_x] = LINE_CHAR

        for p in projected_points:
            if 0 <= p[0] < WIDTH and 0 <= p[1] < HEIGHT:
                grid[p[1]][p[0]] = POINT_CHAR

        output = []
        for row in grid:
            output.append("".join(row))

        print("\033[H" + "\n".join(output), flush=True)

        angle += SPEED
        time.sleep(0.03)

except KeyboardInterrupt:
    clear()
