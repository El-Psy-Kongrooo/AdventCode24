
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
        if left_numbers[i]>right_numbers[i]:
            result+=left_numbers[i]-right_numbers[i]
        if right_numbers[i]>left_numbers[i]:
            result+=right_numbers[i]-left_numbers[i]
        else:
            result+=0
    return result

def main():
    getLists()
    result= getResult()
    print("The distance is: " + str(result))
main()