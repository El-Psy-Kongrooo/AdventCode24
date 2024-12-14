import re
import math

def parse_claw_machines_from_file(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        input_text = file.read()
    
    # Regular expression to match each group (Button A, Button B, Prize)
    pattern = r"Button A: X\+(-?\d+), Y\+(-?\d+)\s+Button B: X\+(-?\d+), Y\+(-?\d+)\s+Prize: X=(-?\d+), Y=(-?\d+)"
    matches = re.findall(pattern, input_text)
    
    # Convert matches to structured data
    machines = []
    for match in matches:
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match)
        machines.append({
            "Button A": {"X": a_x, "Y": a_y},
            "Button B": {"X": b_x, "Y": b_y},
            "Prize": {"X": prize_x, "Y": prize_y}
        })
    
    return machines

def is_nearly_integer(value, tolerance=1e-4):
    return abs(value - round(value)) < tolerance

def getTokens(machine, n):
    a_x, a_y = machine["Button A"]["X"], machine["Button A"]["Y"]
    b_x, b_y = machine["Button B"]["X"], machine["Button B"]["Y"]
    prize_x, prize_y = machine["Prize"]["X"] + 10000000000000, machine["Prize"]["Y"] + 10000000000000
    
    determinant = a_x * b_y - a_y * b_x
    if determinant == 0:
        return 0
    
    D = 1 / determinant
    inv_a_x = b_y * D
    inv_a_y = -b_x * D
    inv_b_x = -a_y * D
    inv_b_y = a_x * D
    
    clicks_a = inv_a_x * prize_x + inv_a_y * prize_y
    clicks_b = inv_b_x * prize_x + inv_b_y * prize_y
    
    if is_nearly_integer(clicks_a):
        clicks_a = round(clicks_a)
    if is_nearly_integer(clicks_b):
        clicks_b = round(clicks_b)

    if clicks_a >= 100 and clicks_b >= 100 and isinstance(clicks_a, int) and isinstance(clicks_b, int):
        tokens = clicks_a * 3 + clicks_b
        print("Tokens for machine ", n, " : ", tokens)
        return tokens
    return 0



def main():
    file_path = "day13_2part.txt"
    parsed_machines = parse_claw_machines_from_file(file_path)
    tokens = 0
    n=1
    for machine in parsed_machines:
        new_tokens= getTokens(machine, n)
        tokens += new_tokens
        n+=1
    print("Total tokens: ", tokens)

main()