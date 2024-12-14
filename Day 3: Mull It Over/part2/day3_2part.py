import re
with open ("day3_2part.txt", 'r') as file:
    total=0
    corrupted_memory  = file.readlines()
    mul_pattern = r'\bmul\(\d+,\d+\)'
    do_like_pattern = r'\b\w*do\(\)\w*'  
    dont_like_pattern = r'\b\w*don\'t\(\)\w*'  

    in_do_block = True 
    for line in corrupted_memory:
        tokens = re.split(r'(\bdo\(\)|\bdon\'t\(\)|mul\(\d+,\d+\))', line)
        
        for token in tokens:
            if re.search(do_like_pattern, token):
                in_do_block = True
            elif re.search(dont_like_pattern, token):
                in_do_block = False
            elif re.search(mul_pattern, token) and in_do_block:
                pattern = r'\bmul\((\d+),(\d+)\)'
                num1, num2 = re.match(pattern, token).groups()
                total += int(num1) * int(num2)
    print(total) 