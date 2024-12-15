def parse_input(warehouse_map_input, movements_input):
    warehouse_map = [list(row) for row in warehouse_map_input.strip().split('\n')]
    movements = movements_input.replace('\n', '')  # Remove newline characters from movements
    return warehouse_map, movements

# Create the new wider map
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
        new_map.append(''.join(new_row))  # Join new row as a string
    return new_map

def robotsMovement(warehouse_map, movements):
    dic = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    
    # Create a mutable copy of the warehouse map at the start
    mutable_warehouse_map = [list(row) for row in warehouse_map]

    # Locate the robot's initial position
    robotCoords = next(
        ((i, row.index('@')) for i, row in enumerate(mutable_warehouse_map) if '@' in row),
        None  
    )
    
    for var in movements:
        robot_x, robot_y = robotCoords
        mov_x, mov_y = dic[var]
        new_x, new_y = robot_x + mov_x, robot_y + mov_y
        
        # Check for collisions
        if mutable_warehouse_map[new_x][new_y] == '#':
            continue

        # Move robot to an empty space
        elif mutable_warehouse_map[new_x][new_y] == '.':
            mutable_warehouse_map[new_x][new_y] = '@'
            mutable_warehouse_map[robot_x][robot_y] = '.'
            robotCoords = (new_x, new_y)

        # Push wide boxes
        elif '[' in mutable_warehouse_map[new_x][new_y] or ']' in mutable_warehouse_map[new_x][new_y]:
            box_chain = []  # Track all boxes in the chain
            stack = [] 
            move_x, move_y = new_x, new_y
            if '[' in mutable_warehouse_map[move_x][move_y]:
                box_chain.append((move_x, move_y, '['))
                box_chain.append((move_x, move_y+1, ']'))
                stack.append((move_x, move_y+1))
                stack.append((move_x, move_y))
            elif ']' in mutable_warehouse_map[move_x][move_y]:
                box_chain.append((move_x, move_y, ']'))
                box_chain.append((move_x, move_y-1, '['))
                stack.append((move_x, move_y-1))
                stack.append((move_x, move_y))
            flag = True

            # Identify the entire chain of wide boxes
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
                        if (curr_x, curr_y+1, ']') not in box_chain:
                            box_chain.append((curr_x, curr_y+1, ']'))
                            stack.append((curr_x, curr_y+1))
                    elif ']' in mutable_warehouse_map[curr_x][curr_y]:
                        if (curr_x, curr_y, ']') not in box_chain:
                            box_chain.append((curr_x, curr_y, ']'))
                            stack.append((curr_x, curr_y))
                        if (curr_x, curr_y-1, '[') not in box_chain:
                            box_chain.append((curr_x, curr_y-1, '['))
                            stack.append((curr_x, curr_y-1))
                    # Move to the next part of the box (consider the wide box extends over two cells)
                    curr_x += mov_x
                    curr_y += mov_y
                    if mutable_warehouse_map[curr_x][curr_y] == '#':
                        flag = False
                        break                

            # After identifying the chain, check if there's space to move the chain
            if flag:  # Space is available for movement

                # Move the entire chain of boxes
                for curr_x, curr_y, form in reversed(box_chain):
                    mutable_warehouse_map[curr_x][curr_y] = '.'
                    next_x, next_y = curr_x + mov_x, curr_y + mov_y
                    mutable_warehouse_map[next_x][next_y] = form

                mutable_warehouse_map[new_x][new_y] = "@"
                mutable_warehouse_map[robot_x][robot_y] = '.'
                robotCoords = (new_x, new_y)

    return mutable_warehouse_map



# Calculate GPS coordinate sum for all boxes
def getNumberBoxes(warehouse_map):
    number = 0
    for x, row in enumerate(warehouse_map):
        for y in range(0, len(row)):  # Step by 2 for wide tiles
            if row[y] == '[':
                number += 100 * x + y # Convert wide coordinates to original format
    return number

# Main function
def main():
    # Read the input from the file
    with open("day15_2part.txt", "r") as file:
        lines = file.read().split("\n\n")  # Split into two parts
        warehouse_map_input = lines[0].strip()
        movements_input = lines[1].strip()

    warehouse_map, movements = parse_input(warehouse_map_input, movements_input)
    wide_warehouse_map = newMap(warehouse_map)

    # Print the wide map
    print("Wide Warehouse Map:")
    for row in wide_warehouse_map:
        print(row)
    print()

    # Simulate robot movement
    new_warehouse_map = robotsMovement(wide_warehouse_map, movements)
    # Print the wide map
    print("Wide Warehouse Map:")
    for row in new_warehouse_map:
        for cell in row:
            print(cell, end="")
        print()

    # Calculate and print the GPS coordinate sum
    numberBoxes = getNumberBoxes(new_warehouse_map)
    print("Sum of GPS coordinates:", numberBoxes)

if __name__ == "__main__":
    main()