def readFile():
    with open("day10_2part.txt", 'r') as file:
        input_grid = [list(line.strip()) for line in file.readlines()]
        return input_grid

def verifyWhereItStarts(grid):
    trailheads = []
    for x,row in enumerate(grid): 
        for y, cell in enumerate(row):
            if cell == '0':
                if (x,y) not in trailheads:
                    trailheads.append((x,y))
    return trailheads

def validCoordenate(coord, grid):
    x, y = coord
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '.':
        return True
    return False

def getCount(x, y, grid):
    stack = [(x, y)] 
    reachable_nines = []
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if validCoordenate((nx, ny), grid):
                current_height = grid[cx][cy]
                neighbor_height = grid[nx][ny]

                if neighbor_height.isdigit() and int(neighbor_height) == int(current_height) + 1:
                    stack.append((nx, ny))

                if neighbor_height == '9' and int(current_height) == 8:
                    reachable_nines.append((nx, ny))

    return len(reachable_nines)

def getTrail(trailheads, grid):
    total_score = 0
    for x, y in trailheads:
        score = getCount(x, y, grid)
        total_score += score
    return total_score

def main():
    input_grid =readFile()

    trailheads = verifyWhereItStarts(input_grid)

    total_score = getTrail(trailheads, input_grid)

    print("The sum of the scores of all trailheads is:", total_score)

main()
