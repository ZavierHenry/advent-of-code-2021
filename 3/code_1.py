
if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, 'r') as reader:
        bits = reader.readline().strip()
        ones_frequency = [ 1 if bit == '1' else 0 for bit in bits ]

        for bits in reader:
            for index,bit in enumerate(bits.strip()):
                ones_frequency[index] += 1 if bit == "1" else -1
        
    gamma = 0
    epsilon = 0
    for index,ones in enumerate(reversed(ones_frequency)):
        if ones > 0:
            gamma |= (1 << index)
        else:
            epsilon |= (1 << index)
    
    print(gamma * epsilon)




