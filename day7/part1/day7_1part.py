def readFile():
    equations = {}
    with open("day7_1part.txt", "r") as file:
        for line in file:
            if line.strip():
                left, right = line.split(":")
                target = int(left.strip())
                numbers = list(map(int, right.strip().split()))
                if target in equations:
                    equations[target].append(numbers)
                else:
                    equations[target] = [numbers]
    return equations

def add(key, values, count):
    if key == count:
        return True
    if len(values) == 0:
        return False
    return (add(key, values[1:], count + values[0]) or mul(key, values[1:], count + values[0]))

def mul(key, values, count):
    if key == count:
        return True
    if len(values) == 0:
        return False
    return (add(key, values[1:], count * values[0]) or mul(key, values[1:], count * values[0]))

def getNumbers(equations):
    listOfValues = []
    for key, equations_list in equations.items():
        for values in equations_list:
            if add(key, values[1:], values[0]) or mul(key, values[1:], values[0]):
                listOfValues.append(key)
    return listOfValues

def main():
    equations = readFile()
    listOfValues = getNumbers(equations)
    totalSum = sum(listOfValues)
    print("Total Sum is", totalSum)

main()
