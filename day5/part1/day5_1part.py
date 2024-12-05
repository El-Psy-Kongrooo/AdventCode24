def parse_input():
    with open("day5_1part.txt", 'r') as file:
        input_data = file.read().strip()

    rules_section, updates_section = input_data.split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(','))) for update in updates_section.splitlines()]
    return rules, updates


def validate_update(update, rules):
    relevant_rules = [(x, y) for x, y in rules if x in update and y in update]
    for x, y in relevant_rules:
        if update.index(x) > update.index(y):
            return False
    return True

def find_middle_sum(valid_updates):
    total_sum = 0
    for update in valid_updates:
        middle = len(update) // 2
        total_sum += update[middle]
    return total_sum


def main():
    rules, updates = parse_input()
    valid_updates = []
    for update in updates:
        if validate_update(update, rules):
            valid_updates.append(update)

    middle_sum = find_middle_sum(valid_updates)
    print("The middle sum is", middle_sum)

main()
