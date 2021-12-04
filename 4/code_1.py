import re

def check_board(board):
    rows = any(all(val is None for val in board[i:i+5]) for i in range(0, 25, 5))
    return rows or any(all(board[j] is None for j in range(i, 25, 5)) for i in range(0, 5))

def update_board(board, value):
    return [ None if val == value else val for val in board ]

def sum_unmarked(board):
    return sum(int(val) for val in board if val is not None)

if __name__ == "__main__":
    filename = "input.txt"

    with open(filename, 'r') as reader:
        numbers = reader.readline().strip().split(',')

        rows = [ re.split("\s+", val.strip()) for index,val in enumerate(reader.readlines()) if index % 6 != 0 ]
        elements = [ val for row in rows for val in row ]
        boards = [ elements[i:i+25] for i in range(0, len(elements), 25)]

    for number in numbers:
        boards = [ update_board(board, number) for board in boards ]
        winners = [ board for board in boards if check_board(board) ]

        if len(winners) > 0:
            break
    
    print(sum_unmarked(winners[0]) * int(number))


