def readFile():   
    with open("day9_2part.txt", 'r') as file:
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

def find_dot_ranges(line):
    result = []
    count = 0
    start = None
    
    for i, char in enumerate(line):
        if char == '.':
            if count == 0:
                start = i  
            count += 1
        else:
            if count > 0:
                result.append([count, start])  
                count = 0  
    if count > 0:
        result.append([count, start])
    
    return result

def processedLine(line):
    first_dot = line.index('.') if '.' in line else -1
    last_int = len(line) - 1 
    flag= True
    while last_int > first_dot:
        if flag:
            dot_ranges = find_dot_ranges(line)  
            flag= False    
        while last_int > first_dot and not isinstance(line[last_int], int):
            last_int -= 1       
        if last_int > first_dot:
            num = line[last_int]
            num_appears = line.count(num)
            for res in dot_ranges:
                dot_count, start = res
                if start > last_int:
                    break
                elif dot_count >= num_appears:
                    for x in range(num_appears):
                        line[start + x] = num
                        line[last_int - x] = '.'
                        flag=True
                    break
            last_int-=num_appears
            if line[first_dot]!='.':          
                first_dot = line.index('.', first_dot + 1) if '.' in line[first_dot + 1:] else -1
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
