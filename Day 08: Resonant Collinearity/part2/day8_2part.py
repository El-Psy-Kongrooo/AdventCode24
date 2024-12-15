from collections import defaultdict
import time
def readFile():   
    # Read the file 
    with open("day8_2part.txt", 'r') as file:
        input_grid = [list(line.strip()) for line in file.readlines()]
    return input_grid

def getAntiNotes(grid):
    coords=[]
    dic = defaultdict(list)
    for x,row in enumerate(grid): 
        for y, cell in enumerate(row):
            if cell != '.':
                    dic[cell].append((x, y))

    for key, values in dic.items():
        for value1 in values:
            for value2 in values:
                if value1!=value2:
                    distX = abs(value1[0] - value2[0])
                    distY = abs(value1[1] - value2[1])
                    first_value = value1
                    second_value = value2
                    while True:
                        if first_value[0] >= second_value[0]:
                            coordX1 = first_value[0] + distX
                        else:
                            coordX1 = first_value[0] - distX
                        
                        if first_value[1]>=second_value[1]:
                            coordY1 = first_value[1] + distY
                        else:
                            coordY1 = first_value[1] - distY
                        if(coordX1>=0 and coordY1>=0 and coordX1 < len(grid) and coordY1 < len(row)):
                            if (coordX1,coordY1) not in coords:
                                coords.append((coordX1,coordY1))
                            first_value, second_value= (coordX1, coordY1), first_value
                        else:
                            break
                    first_value = value1
                    second_value = value2
                    while True:
                        if first_value[0] >= second_value[0]:
                            coordX2 = second_value[0] - distX
                        else:
                            coordX2 = second_value[0] + distX
                        
                        if first_value[1] >= second_value[1]:
                            coordY2 = second_value[1] - distY
                        else:
                            coordY2 = second_value[1] + distY
                        if(coordX2>=0 and coordY2>=0 and coordX2 < len(grid) and coordY2 < len(row)):
                            if (coordX2,coordY2) not in coords:
                                coords.append((coordX2,coordY2))
                            first_value, second_value = second_value, (coordX2, coordY2) 
                        else:
                            break
    for coord in coords:
        if grid[coord[0]][coord[1]]=='.':
            grid[coord[0]][coord[1]] = '#'
            
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # up, down, left, right
        (-1, -1), (-1, 1), (1, -1), (1, 1) # diagonals
    ]
    for x,row in enumerate(grid): 
        for y, cell in enumerate(row):
            if cell != '.' and cell!='#' and (x,y) not in coords:
                 new_x=x
                 new_y=y
                 count=0
                 flag=False
                 for dx,dy in directions:
                    if flag:
                        break
                    while 0<= new_x+dx < len(grid) and 0<= new_y+dy <len(row):
                        new_x= new_x+dx
                        new_y= new_y+dy
                        if grid[new_x][new_y]=='#':
                            count+=1
                        if count>=2:
                            coords.append((x,y))
                            flag=True
                            break

    return grid, coords

def main():
    input_grid = readFile()

    grid, coords = getAntiNotes(input_grid)

    numberAntiNodes = len(coords)

    with open("AntiNodes.txt", 'w') as file:
        for row in grid:
            file.write(''.join(row) + '\n')

    print("Number of AntiNodes is:", numberAntiNodes)

main()

