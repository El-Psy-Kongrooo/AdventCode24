def calculate_total_cost(grid):
    row, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(row)]
    total_cost = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def dfs(i, j):
        visited[i][j] = True
        plant_type = grid[i][j]
        stack = [(i, j)]
        perimeter, area = 0, 0
        while stack:
            ci, cj = stack.pop()
            area += 1
            for dx, dy in directions:
                ni, nj = ci + dx, cj + dy
                if 0 <= ni < row and 0 <= nj < cols:
                    if grid[ni][nj] == plant_type:
                        if not visited[ni][nj]:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1
        return perimeter, area
    
    for i in range(row):
        for j in range(cols):
            if not visited[i][j]:
                perimeter, area = dfs(i, j)
                total_cost += perimeter * area
    return total_cost
                

def main():
    with open("day12_1part.txt") as f:
        grid = [line.strip() for line in f]
    print(calculate_total_cost(grid))

main()