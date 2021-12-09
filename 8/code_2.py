import re

def solve(codes):
    config = [None for i in range(10)]
    config[1] = next(code for code in codes if len(code) == 2)
    config[7] = next(code for code in codes if len(code) == 3)
    config[4] = next(code for code in codes if len(code) == 4)
    config[8] = next(code for code in codes if len(code) == 7)
    
    config[9] = solve_nine(config[4], codes)
    config[0] = solve_zero(config[1], config[9], codes)
    config[6] = solve_six(config[9], config[0], codes)
    config[5] = solve_five(config[6], codes)
    config[3] = solve_three(config[1], codes)

    config[2] = next(code for code in codes if code not in config)

    return config


def solve_nine(four, codes):
    return next(code for code in codes if len(code) == 6 and all(x in code for x in four))

def solve_zero(one, nine, codes):
    return next(code for code in codes if len(code) == 6 and code != nine and all(x in code for x in one))

def solve_six(nine, zero, codes):
    return next(code for code in codes if len(code) == 6 and code != nine and code != zero)

def solve_five(six, codes):
    return next(code for code in codes if len(code) == 5 and all(x in six for x in code))

def solve_three(one, codes):
    return next(code for code in codes if len(code) == 5 and all(x in code for x in one))

def calc_result(result, config : list[str]):
    return int(''.join(str(config.index(x)) for x in result))

if __name__ == "__main__":

    value = 0
    with open('input.txt', 'r') as reader:
        for line in reader:
            m = re.match(r'((?:[a-g]+ )+)\|((?: [a-g]+)+)', line.strip())
            codes = [set(x) for x in  m[1].strip().split(' ')]
            result = [set(x) for x in m[2].strip().split(' ')]
            config = solve(codes)
            value += calc_result(result, config)
    print(value)