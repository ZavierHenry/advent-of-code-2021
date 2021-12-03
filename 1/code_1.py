import requests

if __name__ == "__main__":
    filename = "advent_day_1_input.txt"
    count = 0
    previous = None
    with open(filename, 'r') as reader:
        for line in reader:
            current = int(line)
            if previous and current > previous:
                count += 1

            previous = current

    print(count)