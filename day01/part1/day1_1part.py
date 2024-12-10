
left_numbers = []
right_numbers = []
result=0
def getLists():
    global left_numbers, right_numbers
    with open('day1_1part.txt', 'r') as file:
        for line in file:
            # Split the line into left and right numbers
            left, right = map(int, line.split())
            left_numbers.append(left)
            right_numbers.append(right)

def getResult():
    global left_numbers, right_numbers, result
    left_numbers.sort()
    right_numbers.sort()
    for i in range(len(left_numbers)):
        result+= abs(left_numbers[i]-right_numbers[i])
    return result

def main():
    getLists()
    result= getResult()
    print("The distance is: " + str(result))
main()