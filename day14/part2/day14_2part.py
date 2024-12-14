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
    christmas_tree_pattern = read_pattern_from_file("tree.txt") 
    for i in range(10000): 
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

        robot_map = [["." for _ in range(101)] for _ in range(103)]
        for robot in robots:
            x = robot["position"]["x"]
            y = robot["position"]["y"]
            robot_map[y][x] = "#"

        if has_tree_pattern(robot_map, christmas_tree_pattern):
            print(f"Robot map after {i + 1} steps:\n")
            print(format_robot_map(robot_map))
            break

    return robot_map

def read_pattern_from_file(file_path):
    with open(file_path, 'r') as file:
        pattern = [line.strip() for line in file.readlines()]
    return pattern

def has_tree_pattern(robot_map, pattern):
    pattern_height = len(pattern)
    pattern_width = len(pattern[0])

    for y in range(103 - pattern_height + 1):  
        for x in range(101 - pattern_width + 1):  
            match_found = True
            for py in range(pattern_height):
                for px in range(pattern_width):
                    if robot_map[y + py][x + px] != "#" and pattern[py][px] == "#":
                        match_found = False
                        break
                if not match_found:
                    break
            if match_found:
                return True
    return False

def format_robot_map(robot_map):
    return "\n".join("".join(row) for row in robot_map)
        


def main():
    file_path = "day14_2part.txt"
    robot_list = parse_robots(file_path)
    moveRobots(robot_list)

main()
