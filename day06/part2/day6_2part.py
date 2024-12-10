import copy
import time

def readFile():   
    # Read the file 
    with open("day6_2part.txt", 'r') as file:
        input_grid = [list(line.strip()) for line in file.readlines()]
        return input_grid

def find_coordinates(grid, target='^'):
    # Find the starting coordinates of the guard 
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == target:
                return (col_index, row_index)

def detectLoops(input_grid):
    pass_counts = {}  # Dictionary to track passes over '#' and 'O'
    rows = len(input_grid)
    cols = len(input_grid[0])
    x_value, y_value = find_coordinates(input_grid)
    directions = [((-1, 0), '^', '|'), ((0, 1), '>', '-'), ((1, 0), 'v', '|'), ((0, -1), '<', '-')]
    dic = 0
    add_plus = False

    while 0 <= x_value < cols and 0 <= y_value < rows:
        direction = directions[dic]
        move = direction[0]
        figure = direction[1]
        movement = direction[2]

        if add_plus:
            movement = '+'
            add_plus = False

        new_x_value = x_value + move[1]
        new_y_value = y_value + move[0]

        # Exit the grid
        if new_x_value < 0 or new_x_value >= cols or new_y_value < 0 or new_y_value >= rows:
            input_grid[y_value][x_value] = movement
            return False

        if input_grid[new_y_value][new_x_value] in ['#', 'O']:
            # Increment pass count for the obstacle
            coord = (new_y_value, new_x_value)
            if coord not in pass_counts:
                pass_counts[coord] = 0
            pass_counts[coord] += 1

            # If more than nine passes, we confirm a loop
            if pass_counts[coord] >= 9:
                return True

            dic = (dic + 1) % 4
            add_plus = True
        else:
            # Valid move
            if input_grid[new_y_value][new_x_value] != '.':
                add_plus = True

            input_grid[new_y_value][new_x_value] = figure
            input_grid[y_value][x_value] = movement

            x_value, y_value = new_x_value, new_y_value

    return False
      


def seeLoop(input_grid, y_value, x_value, dic, normal):
    # Determine possible obstruction positions ('O') that create loops
    directions = [((-1, 0), '^', '|'), ((0, 1), '>', '-'), ((1, 0), 'v', '|'), ((0, -1), '<', '-')]
    if  not normal:
        if(dic==0):
            dic=3
        else:
            dic-=1
    move = directions[dic][0]
    loop_coords = []

    if 0 <= y_value < len(input_grid) and 0 <= x_value < len(input_grid[0]) and input_grid[y_value][x_value] == '.':
        input_grid[y_value][x_value] = 'O'  # Mark obstruction position
        original_input = copy.deepcopy(input_grid)
        if detectLoops(original_input):
            loop_coords.append((y_value, x_value))
        input_grid[y_value][x_value] = '.'
    print(loop_coords)
    return loop_coords

def getPaths(input_grid):
    original_input = copy.deepcopy(input_grid)
    Loops = []  # Store loop-forming coordinates

    rows = len(input_grid)
    cols = len(input_grid[0])
    x_value, y_value = find_coordinates(input_grid)
    directions = [((-1, 0), '^', '|'), ((0, 1), '>', '-'), ((1, 0), 'v', '|'), ((0, -1), '<', '-')]
    dic = 0
    add_plus_hash = False
    add_plus_normal = False
    if input_grid[y_value-1][x_value]=='.':
        normal= True
    else:
        normal= False
    while 0 <= x_value < cols and 0 <= y_value < rows:
        direction = directions[dic]    
        move = direction[0]
        figure = direction[1]
        movement = direction[2]

        if add_plus_normal:
            movement = '+'
            add_plus_normal = False 
            normal= True
        if add_plus_hash:
            movement = '+'
            add_plus_hash = False 
            normal= False

        new_x_value = x_value + move[1]
        new_y_value = y_value + move[0]

        if (new_x_value < 0 or new_x_value >= cols) or (new_y_value < 0 or new_y_value >= rows):
            input_grid[y_value][x_value] = movement
            O_Coords = seeLoop(original_input, y_value, x_value, dic, normal)
            for Coord in O_Coords:
                if Coord not in Loops:
                    Loops.append(Coord)
            break
        elif input_grid[new_y_value][new_x_value] == '#':
            dic = (dic + 1) % 4
            add_plus_hash = True
        else:
            # Valid move
            if input_grid[new_y_value][new_x_value] != '.':
                add_plus_normal = True 

            input_grid[new_y_value][new_x_value] = figure
            input_grid[y_value][x_value] = movement
            O_Coords = seeLoop(original_input, y_value, x_value, dic, normal)
            for Coord in O_Coords:
                if Coord not in Loops:
                    Loops.append(Coord)
            x_value, y_value = new_x_value, new_y_value

    return Loops

def main():
    input_grid = readFile()

    loops = getPaths(input_grid)

    print("The number of possible loops is", len(loops))

    with open("Xs.txt", 'w') as file:
        for row in input_grid:
            file.write(''.join(row) + '\n')

# Run the main function
main()
