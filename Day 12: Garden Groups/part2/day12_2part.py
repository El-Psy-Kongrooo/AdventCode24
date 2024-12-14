def calculate_total_cost_with_sides(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visual_grid = [[" " for _ in range(2 * cols + 1)] for _ in range(2 * rows + 1)]
    total_cost = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        visited[i][j] = True
        plant_type = grid[i][j]
        stack = [(i, j)]
        area = 0
        sides = 0
        puzzle_piece = [[" " for _ in range(2 * cols + 1)] for _ in range(2 * rows + 1)]

        while stack:
            ci, cj = stack.pop()
            area += 1
            draw_cell(ci, cj, plant_type, puzzle_piece)
            draw_cell(ci, cj, plant_type, visual_grid)
            for dx, dy in directions:
                ni, nj = ci + dx, cj + dy
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] != plant_type:
                    continue
                elif not visited[ni][nj]:
                    visited[ni][nj] = True
                    stack.append((ni, nj))

        trimmed_piece = trim_visual_grid(puzzle_piece)
        sides = get_sides(trimmed_piece)
        print("Puzzle Piece:")
        print_visual_grid(trimmed_piece)

        return area, sides

    def get_sides(trimmed_piece):
        sides = 0
        for i in range(len(trimmed_piece)):
            previous = 0
            flag = True
            for j in range(len(trimmed_piece[0])):
                if previous == 0:
                    previous = trimmed_piece[i][j]
                elif i-1 >= 0 and i+1 < len(trimmed_piece) and j-1 >= 0 and j+1 < len(trimmed_piece[0]) and trimmed_piece[i][j] == "+" and trimmed_piece[i-1][j] == "|" and trimmed_piece[i+1][j] == "|" and trimmed_piece[i][j-1] == "-" and trimmed_piece[i][j+1] == "-":
                    flag = True
                elif flag and trimmed_piece[i][j] == "-":
                    sides += 1 
                    flag = False
                elif trimmed_piece[i][j] == " " or trimmed_piece[i][j] == previous:
                    flag = True
                previous = trimmed_piece[i][j]

        for j in range(len(trimmed_piece[0])):
            previous = 0
            flag = True
            for i in range(len(trimmed_piece)):
                if previous == 0:
                    previous = trimmed_piece[i][j]
                elif i-1 >= 0 and i+1 < len(trimmed_piece) and j-1 >= 0 and j+1 < len(trimmed_piece[0]) and trimmed_piece[i][j] == "+" and trimmed_piece[i-1][j] == "|" and trimmed_piece[i+1][j] == "|" and trimmed_piece[i][j-1] == "-" and trimmed_piece[i][j+1] == "-":
                    flag = True
                elif flag and trimmed_piece[i][j] == "|":
                    sides += 1
                    flag = False
                elif trimmed_piece[i][j] == " " or trimmed_piece[i][j] == previous:
                    flag = True
                previous = trimmed_piece[i][j]

        print(sides)
        return sides

    def draw_cell(i, j, plant_type, target_grid):
        top_row, left_col = 2 * i, 2 * j
        target_grid[top_row + 1][left_col + 1] = plant_type
        if i == 0 or grid[i - 1][j] != plant_type:
            target_grid[top_row][left_col] = "+"
            target_grid[top_row][left_col + 1] = "-"
            target_grid[top_row][left_col + 2] = "+"
        if i == rows - 1 or grid[i + 1][j] != plant_type:
            target_grid[top_row + 2][left_col] = "+"
            target_grid[top_row + 2][left_col + 1] = "-"
            target_grid[top_row + 2][left_col + 2] = "+"
        if j == 0 or grid[i][j - 1] != plant_type:
            target_grid[top_row][left_col] = "+"
            target_grid[top_row + 1][left_col] = "|"
            target_grid[top_row + 2][left_col] = "+"
        if j == cols - 1 or grid[i][j + 1] != plant_type:
            target_grid[top_row][left_col + 2] = "+"
            target_grid[top_row + 1][left_col + 2] = "|"
            target_grid[top_row + 2][left_col + 2] = "+"

    def trim_visual_grid(v_grid):
        v_grid = [row for row in v_grid if any(cell != " " for cell in row)]
        v_grid = list(map(list, zip(*v_grid)))
        v_grid = [row for row in v_grid if any(cell != " " for cell in row)]
        v_grid = list(map(list, zip(*v_grid)))
        return v_grid

    def print_visual_grid(target_grid):
        for row in target_grid:
            print("".join(row))

    def save_visual_grid_to_file(target_grid, filename):
        with open(filename, "w") as f:
            for row in target_grid:
                f.write("".join(row) + "\n")

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, sides = dfs(i, j)
                total_cost += area * sides

    save_visual_grid_to_file(visual_grid, "visual_grid.txt")
    return total_cost

def main():
    with open("day12_2part.txt") as f:
        grid = [line.strip() for line in f]
    print("Total Cost:", calculate_total_cost_with_sides(grid))

main()
