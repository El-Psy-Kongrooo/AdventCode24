import time
def readFile():   
    with open("day6_1part.txt", 'r') as file:
        input_grid = [list(line.strip()) for line in file.readlines()]
        return input_grid

def find_coordinates(grid, target='^'):
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == target:
                return (col_index, row_index)

def getPaths(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0])
    numberofXs = 0
    x_value, y_value = find_coordinates(input_grid)
    directions = [((0, -1), '^'), ((1, 0), '>'), ((0, 1), 'v'), ((-1, 0), '<')]
    dic = 0

    while 0 <= x_value < cols and 0 <= y_value < rows:
        direction = directions[dic]
        move = direction[0]
        figure = direction[1]
        new_x_value = x_value + move[0]
        new_y_value = y_value + move[1]

        if (new_x_value < 0 or new_x_value >= cols) or (new_y_value < 0 or new_y_value >= rows):
            input_grid[y_value][x_value] = "X"
            with open("Xs.txt", 'w') as file:
                for row in input_grid:
                    file.write(''.join(row) + '\n')
            break
        elif input_grid[new_y_value][new_x_value] == '#':
            dic += 1
            if dic == 4:
                dic = 0
        else:
            input_grid[new_y_value][new_x_value] = figure
            input_grid[y_value][x_value] = "X"
            x_value, y_value = new_x_value, new_y_value
            with open("Xs.txt", 'w') as file:
                for row in input_grid:
                    file.write(''.join(row) + '\n')
            #can be removed the comment bellow to see it working on Xs.txt
            #time.sleep(0.1) #can be removed
    return input_grid

def getXs(grid):
    numberOfXs= 0
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 'X':
                numberOfXs+=1
    return numberOfXs

def main():
    input_grid = readFile()
    input_grid = getPaths(input_grid)
    numberOfXs = getXs(input_grid)
    print("The number of steps it took was", numberOfXs)

main()
