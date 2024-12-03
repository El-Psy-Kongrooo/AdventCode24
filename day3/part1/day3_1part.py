import re
with open ("day3_1part.txt", 'r') as file:
    total=0
    corrupted_memory  = file.read()
    # Regex pattern to match only `mul(int,int)` with integers
    pattern = r'\bmul\(\d+,\d+\)'

    matches = re.findall(pattern, corrupted_memory)

    for mul in matches:
        # Regex pattern to capture numbers inside `mul(int,int)`
        pattern = r'\bmul\((\d+),(\d+)\)'
        num1, num2 = re.match(pattern, mul).groups()
        total+=int(num1)*int(num2)
    print(total)
