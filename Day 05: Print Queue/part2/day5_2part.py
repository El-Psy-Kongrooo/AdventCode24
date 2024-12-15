def parse_input():
    with open("day5_2part.txt", 'r') as file:
        input_data = file.read().strip()

    rules_section, updates_section = input_data.split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(','))) for update in updates_section.splitlines()]
    return rules, updates


def validate_update_incorrect(update, rules):
    relevant_rules = [(x, y) for x, y in rules if x in update and y in update]
    while True:
        retry = False
        for x, y in relevant_rules:
            if update.index(x) > update.index(y):
                dx = update.index(x)
                dy = update.index(y)

                update[dx], update[dy] = update[dy], update[dx]
                retry= True
        if not retry:
            return update
        
def validate_update_correct(update, rules):
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
        if validate_update_correct(update, rules):
            valid_updates.append(update)
    middle_sum_correct = find_middle_sum(valid_updates)

    invalid_updates = []

    for update in updates:
        update = validate_update_incorrect(update, rules)
        invalid_updates.append(update)
    middle_sum_incorrect = find_middle_sum(invalid_updates)
    
    middle_sum= middle_sum_incorrect-middle_sum_correct
    print("The middle sum is", middle_sum)

main()
