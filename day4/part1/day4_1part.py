def readFile():   
    with open ("day4_1part.txt", 'r') as file:
        input_XMAS = [line.strip() for line in file.readlines()]
        return input_XMAS

def getXMASNumber(input_XMAS, word):
    size= len(word)
    count=0
    rows=len(input_XMAS)
    cols=len(input_XMAS[0])
    new_list = [["." for _ in range(cols)] for _ in range(rows)]
    directions=[
        [1,0],   #down
        [-1,0],  #up
        [0,1],   #right
        [0,-1],  #left
        [1,-1],  #diagonal down-left
        [1,1],   #diagonal down-right
        [-1,1],  #diagonal up-right
        [-1,-1]  #diagonal up-left
    ]

    def valid_points(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_word(dx,dy,x,y):
        list_xy=[]
        for k in range(size):
            nx,ny= x+dx*k, y+dy*k
            if not valid_points(nx,ny) or input_XMAS[nx][ny]!=word[k]:
                return False
            list_xy.append([nx,ny])
        for line in list_xy:
            nx, ny= line[0], line[1]
            new_list[nx][ny]= input_XMAS[nx][ny]
        return True

    for i in range(rows):
        for j in range(cols):
            if input_XMAS[i][j]==word[0]:
                for dx,dy in directions:
                    if check_word(dx,dy,i,j):
                        count+=1
    return count, new_list

def main():
    input_XMAS= readFile()
    result, xmas_list = getXMASNumber(input_XMAS, "XMAS")
    with open("XMAS.txt", "w") as file:
        for row in xmas_list:
            file.write("".join(row) + "\n")
    print("New grid in XMAS.txt")
    print("Number of XMAS:", result)

main()