from collections import defaultdict

def readFile():   
    with open("day8_1part.txt", 'r') as file:
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
                    if value1[0]>=value2[0]:
                        coordX1 = value1[0] + distX
                        coordX2 = value2[0] - distX
                    else:
                        coordX1 = value1[0] - distX
                        coordX2 = value2[0] + distX
                    
                    if value1[1]>=value2[1]:
                        coordY1 = value1[1] + distY
                        coordY2 = value2[1] - distY
                    else:
                        coordY1 = value1[1] - distY
                        coordY2 = value2[1] + distY
                    if(coordX1>=0 and coordY1>=0 and coordX1 < len(grid) and coordY1 < len(row)):
                        if (coordX1,coordY1) not in coords:
                            coords.append((coordX1,coordY1))
                    if(coordX2>=0 and coordY2>=0 and coordX2 < len(grid) and coordY2 < len(row)):
                        if (coordX2,coordY2) not in coords:
                            coords.append((coordX2,coordY2))
    for coord in coords:
        if grid[coord[0]][coord[1]]=='.':
            grid[coord[0]][coord[1]] = '#'
    
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

