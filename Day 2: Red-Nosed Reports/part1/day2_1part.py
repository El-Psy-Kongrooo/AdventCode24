def getLists():
    reportsList = []
    with open("day2_1part.txt", "r") as file:
        for line in file:
            reportsList.append(list(map(int, line.strip().split())))
    return reportsList


def is_increasing_or_decreasing(report):
    increasing = all(report[i + 1] > report[i] for i in range(len(report) - 1))
    decreasing = all(report[i + 1] < report[i] for i in range(len(report) - 1))
    return increasing or decreasing


def is_valid(report):
    differences = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
    return all(1 <= diff <= 3 for diff in differences)


def count_safe_reports(reports):
    safe_count = 0

    for report in reports:
        if is_increasing_or_decreasing(report) and is_valid(report):
            safe_count += 1

    return safe_count


def main():
    reports = getLists()
    safe_count = count_safe_reports(reports)
    print("Number of valid reports:", safe_count)


# Execute the main function
main()
