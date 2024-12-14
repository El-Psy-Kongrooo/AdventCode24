def parse_robots(file_path):
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  
                parts = line.split()
                position = tuple(map(int, parts[0][2:].split(',')))
                velocity = tuple(map(int, parts[1][2:].split(',')))
                robots.append({"position": {"x": position[0], "y": position[1]}, 
                               "velocity": {"x": velocity[0], "y": velocity[1]}})
    return robots

def moveRobots(robots):
    for _ in range(100):
        for robot in robots:
            x = robot["position"]["x"]
            y = robot["position"]["y"]
            vx = robot["velocity"]["x"]
            vy = robot["velocity"]["y"]
            if x + vx < 0:
                robot["position"]["x"] = 101 + (vx + x)
            elif x + vx > 100:
                robot["position"]["x"] = (x + vx - 101)
            else:
                robot["position"]["x"] = x + vx
            if y + vy < 0:
                robot["position"]["y"] = 103 + (vy + y)
            elif y + vy > 102:
                robot["position"]["y"] = (y + vy - 103)
            else:
                robot["position"]["y"] = y + vy

    robot_map = [[0 for _ in range(101)] for _ in range(103)]
    for robot in robots:
        x = robot["position"]["x"]
        y = robot["position"]["y"]
        robot_map[y][x] += 1
    return robot_map

def getRobots(robot_map):
    listRobots = []
    
    # Quadrant 1: Top-left
    numRobots = 0
    for row in robot_map[:51]:
        for cell in row[:50]:
            numRobots += cell
    listRobots.append(numRobots)

    # Quadrant 2: Top-right
    numRobots = 0
    for row in robot_map[:51]:
        for cell in row[51:]:
            numRobots += cell
    listRobots.append(numRobots)

    # Quadrant 3: Bottom-right
    numRobots = 0
    for row in robot_map[52:]:
        for cell in row[51:]:
            numRobots += cell
    listRobots.append(numRobots)

    # Quadrant 4: Bottom-left
    numRobots = 0
    for row in robot_map[52:]:
        for cell in row[:50]:
            numRobots += cell
    listRobots.append(numRobots)

    return listRobots

def main():
    file_path = "day14_1part.txt"
    robot_list = parse_robots(file_path)
    robot_map = moveRobots(robot_list)
    quadrant_counts = getRobots(robot_map)
    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count
    print("Quadrant counts:", quadrant_counts)
    print("Safety factor:", safety_factor)

main()
