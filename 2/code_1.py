import re


if __name__ == "__main__":
    filename = "day_2_input.txt"
    horizontal_position = 0
    vertical_position = 0

    with open(filename, 'r') as reader:
        for line in reader:
            m = re.match("^(\w+) (\d+)$", line)
            command = m[1]
            unit = int(m[2])

            if command == "forward":
                horizontal_position += unit
            elif command == "down":
                vertical_position += unit
            elif command == "up":
                vertical_position -= unit

    print("Position:", (horizontal_position, vertical_position))
    print("Answer:", horizontal_position * vertical_position)
