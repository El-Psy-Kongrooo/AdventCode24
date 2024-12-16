import heapq

def calculate_min_move(grid):
    start = None
    end = None
    for i, row in enumerate(grid):
        if 'S' in row:
            start = (i, row.index('S'))
        if 'E' in row:
            end = (i, row.index('E'))
    
    if not start or not end:
        raise ValueError("Start or end position not found in the grid")

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
    dir_symbols = ['>', 'v', '<', '^']  # Symbols to represent directions

    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0, []))  # (cost, x, y, direction, path)

    # Visited dictionary: (x, y, direction) -> cost
    visited = {}

    while pq:
        cost, x, y, direction, path = heapq.heappop(pq)
        if (x, y) == end:
            final_grid = [list(row) for row in grid]
            for px, py, pd in path:
                if final_grid[px][py] not in ('S', 'E'):
                    final_grid[px][py] = dir_symbols[pd]
            print("\n".join("".join(row) for row in final_grid))
            return cost

        if (x, y, direction) in visited and visited[(x, y, direction)] <= cost:
            continue
        
        visited[(x, y, direction)] = cost

        for i, (dy, dx) in enumerate(directions):
            if (direction + 2) % 4 == i:  
                continue

            nx, ny = x + dy, y + dx

            if i == direction: 
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                    heapq.heappush(pq, (cost + 1, nx, ny, direction, path + [(nx, ny, direction)]))

            else:
                rotation_cost = 1000
                new_direction = i
                heapq.heappush(pq, (cost + rotation_cost, x, y, new_direction, path))

    return -1  

def main():
    with open("day16_1part.txt") as f:
        grid = [line.strip() for line in f]
    print(calculate_min_move(grid))

if __name__ == "__main__":
    main()