import re

def generate_points(x1, y1, x2, y2, board_size):
    if y1 == y2:
        return range(y1*board_size + min(x1, x2), y1*board_size + max(x1, x2) + 1)
    else:
        return range(min(y1, y2)*board_size + x1, max(y1, y2)*board_size + x1 + 1, board_size)

if __name__ == "__main__":

    lines = []
    with open("input.txt", 'r') as reader:
        
        for line in reader:
            m = re.match(r'^(\d+),(\d+) -> (\d+),(\d+)', line.strip())
            if m[1] == m[3] or m[2] == m[4]:
                x1 = int(m[1])
                y1 = int(m[2])
                x2 = int(m[3])
                y2 = int(m[4])
                lines.append([x1, y1, x2, y2])
        
    board_size = max(max(x1, x2) for x1,y1,x2,y2 in lines) + 1
    points = set()
    intersection = set()

    for x1,y1,x2,y2 in lines:
        points_range = [ x for x in generate_points(x1, y1, x2, y2, board_size)]
        intersection.update(points.intersection(points_range))
        points.update(points_range)
    
    print(len(intersection))
        


    







