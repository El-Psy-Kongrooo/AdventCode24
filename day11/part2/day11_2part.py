from collections import Counter, defaultdict

def readFile():
    with open("day11_2part.txt", 'r') as file:
        line = file.readline().strip()
        numbers = list(map(int, line.split()))
        return numbers

def blink(numbers):
    blink = 0
    numbers = Counter(numbers)
    while blink < 75:
        new_numbers = defaultdict(int)
        for stone, _ in numbers.items():
            num_str = str(stone)
            if stone == 0:
                new_numbers[1] += numbers[0]
            elif len(num_str) % 2 == 0:
                midpoint = len(num_str) // 2
                left = int(num_str[:midpoint])
                right = int(num_str[midpoint:])
                new_numbers[left] += numbers[stone]
                new_numbers[right] += numbers[stone]
            else:
                new_numbers[stone * 2024] += numbers[stone]
        blink += 1
        print(f"After {blink} blinks, number of stones is {sum(new_numbers.values())}")
        numbers = new_numbers
    return new_numbers

def main():
    numbers = readFile()
    new_numbers = blink(numbers)
    print("Final number of stones:", sum(new_numbers.values()))

main()
