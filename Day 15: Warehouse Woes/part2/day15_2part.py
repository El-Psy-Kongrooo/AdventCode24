def parse_input(warehouse_map_input, movements_input):
    warehouse_map = [list(row) for row in warehouse_map_input.strip().split('\n')]
    movements = movements_input.replace('\n', '')
    return warehouse_map, movements

def newMap(warehouse_map):
    new_map = []
    for row in warehouse_map:
        new_row = []
        for cell in row:
            if cell == '#':
                new_row.append('##')
            elif cell == '.':
                new_row.append('..')
            elif cell == 'O':
                new_row.append('[]')
            elif cell == '@':
                new_row.append('@.')
        new_map.append(''.join(new_row))
    return new_map

def find_occurrences(warehouse_map, search_str):
    occurrences = []
    for i, row in enumerate(warehouse_map):
        row_str = ''.join(row)
        start = 0
        while True:
            idx = row_str.find(search_str, start)
            if idx == -1:
                break
            occurrences.append((i, idx))
            start = idx + 1
    return occurrences

def robotsMovement(warehouse_map, movements):
    dic = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    mutable_warehouse_map = [list(row) for row in warehouse_map]
    robotCoords = next(((i, row.index('@')) for i, row in enumerate(mutable_warehouse_map) if '@' in row), None)
    n = 0
    for var in movements:
        n += 1
        robot_x, robot_y = robotCoords
        mov_x, mov_y = dic[var]
        new_x, new_y = robot_x + mov_x, robot_y + mov_y
        
        if mutable_warehouse_map[new_x][new_y] == '#':
            continue

        elif mutable_warehouse_map[new_x][new_y] == '.':
            mutable_warehouse_map[new_x][new_y] = '@'
            mutable_warehouse_map[robot_x][robot_y] = '.'
            robotCoords = (new_x, new_y)

        elif '[' in mutable_warehouse_map[new_x][new_y] or ']' in mutable_warehouse_map[new_x][new_y]:
            box_chain = []
            stack = [] 
            move_x, move_y = new_x, new_y
            if '[' in mutable_warehouse_map[move_x][move_y]:
                box_chain.append((move_x, move_y, '['))
                box_chain.append((move_x, move_y + 1, ']'))
                stack.append((move_x, move_y + 1))
                stack.append((move_x, move_y))
            elif ']' in mutable_warehouse_map[move_x][move_y]:
                box_chain.append((move_x, move_y, ']'))
                box_chain.append((move_x, move_y - 1, '['))
                stack.append((move_x, move_y - 1))
                stack.append((move_x, move_y))
            flag = True

            while stack and flag:
                curr_x, curr_y = stack.pop()
                curr_x += mov_x
                curr_y += mov_y
                if mutable_warehouse_map[curr_x][curr_y] == '#':
                    flag = False
                    break
                while '[' in mutable_warehouse_map[curr_x][curr_y] or ']' in mutable_warehouse_map[curr_x][curr_y]:
                    if '[' in mutable_warehouse_map[curr_x][curr_y]:
                        if (curr_x, curr_y, '[') not in box_chain:
                            box_chain.append((curr_x, curr_y, '['))
                            stack.append((curr_x, curr_y))
                        if (curr_x, curr_y + 1, ']') not in box_chain:
                            box_chain.append((curr_x, curr_y + 1, ']'))
                            stack.append((curr_x, curr_y + 1))
                    elif ']' in mutable_warehouse_map[curr_x][curr_y]:
                        if (curr_x, curr_y, ']') not in box_chain:
                            box_chain.append((curr_x, curr_y, ']'))
                            stack.append((curr_x, curr_y))
                        if (curr_x, curr_y - 1, '[') not in box_chain:
                            box_chain.append((curr_x, curr_y - 1, '['))
                            stack.append((curr_x, curr_y - 1))
                    curr_x += mov_x
                    curr_y += mov_y
                    if mutable_warehouse_map[curr_x][curr_y] == '#':
                        flag = False
                        break                

            if flag:
                for curr_x, curr_y, form in reversed(box_chain):
                    mutable_warehouse_map[curr_x][curr_y] = '.'
                    next_x, next_y = curr_x + mov_x, curr_y + mov_y
                    mutable_warehouse_map[next_x][next_y] = form

                mutable_warehouse_map[new_x][new_y] = "@"
                mutable_warehouse_map[robot_x][robot_y] = '.'
                robotCoords = (new_x, new_y)

            if find_occurrences(mutable_warehouse_map, '[.'):  
                for i, j in find_occurrences(mutable_warehouse_map, '[.'):
                    mutable_warehouse_map[i][j] = '['
                    mutable_warehouse_map[i][j + 1] = ']'

            if find_occurrences(mutable_warehouse_map, '.]'):  
                for i, j in find_occurrences(mutable_warehouse_map, '.]'):
                    mutable_warehouse_map[i][j] = '['
                    mutable_warehouse_map[i][j - 1] = ']'
                
    return mutable_warehouse_map

def getNumberBoxes(warehouse_map):
    number = 0
    for x, row in enumerate(warehouse_map):
        for y in range(0, len(row)):
            if row[y] == '[':
                number += 100 * x + y
    return number

def main():
    with open("day15_2part.txt", "r") as file:
        lines = file.read().split("\n\n")
        warehouse_map_input = lines[0].strip()
        movements_input = lines[1].strip()

    warehouse_map, movements = parse_input(warehouse_map_input, movements_input)
    wide_warehouse_map = newMap(warehouse_map)

    new_warehouse_map = robotsMovement(wide_warehouse_map, movements)

    numberBoxes = getNumberBoxes(new_warehouse_map)
    print("Sum of GPS coordinates:", numberBoxes)

    with open("new_warehouse_map.txt", "w") as output_file:
        for row in new_warehouse_map:
            output_file.write(''.join(row) + "\n")

if __name__ == "__main__":
    main()
