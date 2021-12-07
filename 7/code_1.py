
def total_distance(center, freq):
    return sum(abs(k-center) * freq[k] for k in freq)


if __name__ == "__main__":

    with open('input.txt', 'r') as reader:
        distances = [x for x in reader.read().strip().split(',')]
    
    freq = { int(k): sum(1 for x in distances if x == k) for k in distances }

    print(min(total_distance(c, freq) for c in freq))