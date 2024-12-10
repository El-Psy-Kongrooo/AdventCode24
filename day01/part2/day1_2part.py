left_numbers = []
right_numbers = []
result = 0

def getLists():
    global left_numbers, right_numbers
    with open('day1_2part.txt', 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_numbers.append(left)
            right_numbers.append(right)

def getResult():
    global left_numbers, right_numbers, result
    left_numbers.sort()
    right_numbers.sort()
    
    rn = 0  
    n = len(right_numbers)
    
    for i in range(len(left_numbers)):
        equal = 0  
        while rn < n:
            if left_numbers[i] == right_numbers[rn]:
                equal += 1
                rn += 1
            elif left_numbers[i] > right_numbers[rn]:
                rn += 1 
            else:  
                break
        result += left_numbers[i] * equal

    return result

def main():
    getLists()
    result = getResult()
    print("The similarity score is:", result)

main()
