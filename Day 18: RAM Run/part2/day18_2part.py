def parse_coordinates(file_path):
    coords = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        x, y = map(float, line.strip().split(","))
        coords.append((x, y))
    return coords

from collections import deque

def bfs_shortest_path(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0, 0)])  
    visited = set()
    parents = {}  
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()

        if (x, y) == (70, 70):
            path = []
            while (x, y) != (0, 0):  
                path.append((x, y))
                x, y = parents[(x, y)]
            path.append((0, 0))
            return path[::-1]  

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x <= 70 and 0 <= new_y <= 70:
                if (new_x, new_y) not in visited and grid[new_y][new_x] == '.':
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
                    parents[(new_x, new_y)] = (x, y)

    return None  


def main():
    file_path = "day18_2part.txt"
    coordinates = parse_coordinates(file_path)
    grid = [['.' for _ in range(71)] for _ in range(71)]
    for x , coord in enumerate(coordinates):
        if x < 1024:
            x, y = map(int, coord)
            grid[y][x] = '#'
    n = 1025
    while n< len(coordinates):
        coord = coordinates[n]
        x, y = map(int, coord)
        grid[y][x] = '#'
        if not bfs_shortest_path(grid):
            print(coord)
            break
        n += 1

if __name__ == "__main__":
    main()
