# Read the input file
def read_input():
    with open('day15_1part.txt', 'r') as file:
        lines = file.read().splitlines()  

    warehouse_map = []
    movements = ""

    # Process lines
    for line in lines:
        if line.startswith('#'): 
            warehouse_map.append(list(line))  
        else:  
            movements += line.strip()  
    return warehouse_map, movements

def robotsMovement(warehouse_map, movements):
    dic = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    
    robotCoords = next(
        ((i, row.index('@')) for i, row in enumerate(warehouse_map) if '@' in row),
        None  
    )
    
    for var in movements:
        robot_x, robot_y = robotCoords
        mov_x, mov_y = dic[var]
        new_x, new_y = robot_x + mov_x, robot_y + mov_y
        
        if warehouse_map[new_x][new_y] == '#':
            continue
        
        elif warehouse_map[new_x][new_y] == '.':
            warehouse_map[new_x][new_y] = '@'
            warehouse_map[robot_x][robot_y] = '.'
            robotCoords = (new_x, new_y)
        

        elif warehouse_map[new_x][new_y] == 'O':
            box_chain = [] 
            move_x, move_y = new_x, new_y
            
            while warehouse_map[move_x][move_y] == 'O':
                box_chain.append((move_x, move_y))
                move_x += mov_x
                move_y += mov_y
            
            if warehouse_map[move_x][move_y] == '.':
                warehouse_map[new_x][new_y] = '@'
                warehouse_map[robot_x][robot_y] = '.'
                robotCoords = (new_x, new_y)
                
                for i in reversed(range(len(box_chain))):
                    curr_x, curr_y = box_chain[i]
                    next_x, next_y = curr_x + mov_x, curr_y + mov_y
                    warehouse_map[next_x][next_y] = 'O'
                    warehouse_map[curr_x][curr_y] = '.'
    return warehouse_map

def getNumberBoxes(warehouse_map):
    number = 0
    for x, row in enumerate(warehouse_map):
        for y, cell in enumerate(row):
            if cell == 'O':
                number += 100*x + y
    return number
                
def main():
    warehouse_map, movements = read_input()
    new_warehouse_map = robotsMovement(warehouse_map, movements)
    with open('new_warehouse_map.txt', 'w') as file:
        for row in new_warehouse_map:
            file.write(''.join(row) + '\n')
    numberBoxes = getNumberBoxes(new_warehouse_map)
    print(numberBoxes)

if __name__ == "__main__":
    main()


