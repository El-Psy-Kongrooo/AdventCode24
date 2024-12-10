def readFile():   
    with open("day9_1part.txt", 'r') as file:
        for line in file.readlines():
            line = list(line.strip()) 
        return line
    
def decompressedLine(line):
    new_line=[]
    flag= True
    x=0
    for num in line:
        for _ in range(int(num)):
            if flag:
                new_line.append(x)
            else:
                new_line.append('.')
        if flag:
            x+=1
        flag= not flag
    return new_line

def processedLine(line):
    first_dot = line.index('.')
    last_int = len(line) - 1
    while last_int > first_dot:
        while last_int > first_dot and not isinstance(line[last_int], int):
            last_int -= 1
        if last_int > first_dot:
            line[first_dot], line[last_int] = line[last_int], '.'
            first_dot = line.index('.', first_dot + 1)
    return line

def sumValLine(line):
    list_num = []
    for x, num in enumerate(line):
        if(isinstance(num,int)):
            list_num.append(int(x)*int(num))
    return list_num

def main():
    line = readFile()
    line_descompressed = decompressedLine(line)
    line_processed = processedLine(line_descompressed)
    list_num = sumValLine(line_processed)
    num = sum(list_num)
    with open("Fragment.txt", 'w') as file:
        file.write(''.join(str(item) for item in line_processed) + '\n')
    print("The filesystem checksum is", num)

main()
