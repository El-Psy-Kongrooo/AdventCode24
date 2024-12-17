# Initialize containers
registers = {}
program = []

def read_file():
    with open('day17_1part.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Register"): 
                key, value = line.split(":")  
                key = key.split()[1]  
                registers[key] = int(value.strip())  
            elif line.startswith("Program"):  
                global program
                program = [int(num) for num in line.split(":")[1].split(",")]  
        return registers, program

def resolve_operand(operand, registers):
    if operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    return operand

def do_Program(registers, program):
    pos = 0
    output = [] 
    while 0 <= pos < len(program):
        opcode = program[pos]
        operand = resolve_operand(program[pos + 1], registers)

        if opcode == 0:  # adv
            registers['A'] = registers['A'] // 2**operand
            pos += 2
        elif opcode == 1:  # bxl
            registers['B'] = registers['B'] ^ operand
            pos += 2
        elif opcode == 2:  # bst
            registers['B'] = operand % 8
            pos += 2
        elif opcode == 3:  # jnz
            if registers['A'] > 0:
                pos = operand
            else:
                pos += 2
        elif opcode == 4:  # bxc
            registers['B'] = registers['B'] ^ registers['C']
            pos += 2
        elif opcode == 5:  # out
            output.append(operand % 8)
            pos += 2
        elif opcode == 6:  # bdv
            registers['B'] = registers['A'] // 2**operand
            pos += 2
        elif opcode == 7:  # cdv
            registers['C'] = registers['A'] // 2**operand
            pos += 2
    return output

def main():
    registers, program = read_file()
    output = do_Program(registers, program)
    print(",".join(map(str, output)))  

main()
