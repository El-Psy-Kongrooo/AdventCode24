import time
def readFile():
     with open("day11_1part.txt", 'r') as file:
        line = file.readline().strip()
        numbers = list(map(int, line.split()))
        return numbers
def blink(numbers):
    blink = 0
    while blink < 25:
        new_numbers = []
        for num in numbers:
            num_str = str(num)
            if num == 0:
                new_numbers.append(1)
            elif len(num_str)%2 == 0:
                midpoint = len(num_str)//2
                left = num_str[:midpoint]
                right = num_str[midpoint:]
                new_numbers.append(int(left))
                new_numbers.append(int(right))
            else:
                new_numbers.append(num*2024)
        blink += 1
        print("After", blink, "blinks, number of stones is")
        print(new_numbers)
        numbers = new_numbers
        time.sleep(1)
    return new_numbers
def main():
    numbers = readFile()
    new_numbers = blink(numbers)
    print("Number of stones",len(new_numbers))

main()