import re

def is_horizontal(x1, y1, x2, y2):
    return y1 == y2

def is_vertical(x1, y1, x2, y2):
    return x1 == x2

def is_diagonal(x1, y1, x2, y2):
    return abs(x1-x2) == abs(y1-y2)

def generate_points(x1, y1, x2, y2, board_size):

    if is_horizontal(x1, y1, x2, y2):
        return range(y1*board_size + min(x1, x2), y1*board_size + max(x1, x2) + 1)
    elif is_vertical(x1, y1, x2, y2):
        return range(min(y1, y2)*board_size + x1, max(y1, y2)*board_size + x1 + 1, board_size)
    else:
        top,bottom = [[x1, y1], [x2, y2]] if y1 < y2 else [[x2, y2], [x1, y1]]
        direction = 1 if top[0] < bottom[0] else -1
        return range(top[1]*board_size + top[0], bottom[1]*board_size + bottom[0] + 1, board_size + direction)

if __name__ == "__main__":

    lines = []
    with open('input.txt', 'r') as reader:

        for line in reader:
            m = re.match(r'^(\d+),(\d+) -> (\d+),(\d+)', line.strip())
            x1 = int(m[1])
            y1 = int(m[2])
            x2 = int(m[3])
            y2 = int(m[4])

            if is_horizontal(x1, y1, x2, y2) or is_vertical(x1, y1, x2, y2) or is_diagonal(x1, y1, x2, y2):
                lines.append([x1, y1, x2, y2])
        
    board_size = max(max(x1, x2) for x1,y1,x2,y2 in lines) + 1
    points = set()
    intersection = set()

    for x1,y1,x2,y2 in lines:
        points_range = [ x for x in generate_points(x1, y1, x2, y2, board_size)]
        intersection.update(points.intersection(points_range))
        points.update(points_range)
    
    print(len(intersection))

