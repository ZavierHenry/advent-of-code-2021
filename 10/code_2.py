
def incomplete_stack(line, match):
    stack = []
    for character in line:
        if character in match and (len(stack) == 0 or match[character] != stack[-1]):
            return None
        elif character in match and match[character] == stack[-1]:
            stack.pop()
        else:
            stack.append(character)
    
    return stack

def get_score(stack, reverse_match):
    score = 0
    for char in reversed(stack):
        reverse_char = reverse_match[char]
        score *= 5
        if reverse_char == ')':
            score += 1
        elif reverse_char == ']':
            score += 2
        elif reverse_char == '}':
            score += 3
        elif reverse_char == '>':
            score += 4
    
    return score


if __name__ == "__main__":

    match = {
        ']': '[',
        ')': '(',
        '>': '<',
        '}': '{'
    }

    reverse_match = { match[k]: k for k in match }

    total = 0
    with open('input.txt', 'r') as reader:
        incomplete = filter(lambda x: x is not None, map(lambda line: incomplete_stack(line.strip(), match), reader.readlines()))
    
    scores = sorted(map(lambda x: get_score(x, reverse_match), incomplete))
    print(len(scores))
    print(scores[len(scores) // 2])