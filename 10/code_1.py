



if __name__ == "__main__":

    match = {
        ']': '[',
        ')': '(',
        '>': '<',
        '}': '{'
    }

    score = {
        ']': 57,
        ')': 3,
        '>': 25137,
        '}': 1197
    }

    total = 0
    with open('input.txt', 'r') as reader:
        for line in reader:
            stack = []
            line = line.strip()
            for character in line:
                if character in match and (len(stack) == 0 or match[character] != stack[-1]):
                    total += score[character]
                    break
                elif character in match and match[character] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(character)
    
    print(total)


