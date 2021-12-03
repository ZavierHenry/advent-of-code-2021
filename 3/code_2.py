
def filter_codes(codes, index, type):
    codes_length = len(codes)
    ones_frequency = sum(1 for code in codes if code[index] == '1')

    if (type == 'max' and ones_frequency >= codes_length / 2) or (type == 'min' and ones_frequency < codes_length / 2):
        return [ code for code in codes if code[index] == '1' ]
    else:
        return [ code for code in codes if code[index] == '0' ]

if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, 'r') as reader:
        codes = [ bits.strip() for bits in reader ]
    
    index = 0
    max_codes = codes
    while len(max_codes) > 1:
        max_codes = filter_codes(max_codes, index, 'max')
        index += 1

    index = 0
    min_codes = codes
    while len(min_codes) > 1:
        min_codes = filter_codes(min_codes, index, 'min')
        index += 1

    print(int(max_codes[0], 2) * int(min_codes[0], 2)) 




