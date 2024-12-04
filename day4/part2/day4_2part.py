def readFile():   
    with open ("day4_2part.txt", 'r') as file:
        input_XMAS = [line.strip() for line in file.readlines()]
        return input_XMAS

def getXMASNumber(input_XMAS, word):
    size= len(word)
    count=0
    rows=len(input_XMAS)
    cols=len(input_XMAS[0])
    new_list = [["." for _ in range(cols)] for _ in range(rows)]
    directions=[
        [-1,1],  #diagonal up-right
        [-1,-1]  #diagonal up-left
    ]

    def valid_points(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_word(x,y):
        list_xy=[]
        for dx, dy in directions:
            nx1,ny1= x+dx, y+dy
            nx2,ny2 = x-dx, y-dy
            if not valid_points(nx1,ny1) or not valid_points(nx2,ny2):
                continue
            if input_XMAS[nx1][ny1]== 'M' and input_XMAS[nx2][ny2]=='S':
                list_xy.append([nx1,ny1])
                list_xy.append([nx2,ny2])
            if input_XMAS[nx1][ny1]== 'S' and input_XMAS[nx2][ny2]=='M':
                list_xy.append([nx1,ny1])
                list_xy.append([nx2,ny2])
        if len(list_xy)==4:
            for line in list_xy:
                nx, ny= line[0], line[1]
                new_list[nx][ny]= input_XMAS[nx][ny]
            new_list[x][y]= word[1]
            return True
        return False
    
    for i in range(rows):
        for j in range(cols):
            if input_XMAS[i][j]=='A':
                if check_word(i,j):
                    count+=1
    return count, new_list

def main():
    input_XMAS= readFile()
    result, xmas_list = getXMASNumber(input_XMAS, "MAS")
    with open("X-MAS.txt", "w") as file:
        for row in xmas_list:
            file.write("".join(row) + "\n")
    print("New grid in X-MAS.txt")
    print("Number of X-MAS:", result)

main()