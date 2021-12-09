import re

if __name__ == "__main__":

    count = 0
    with open('example.txt', 'r') as reader:
        for line in reader:
            m = re.search(r'\| ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+)', line)
            count += sum(1 for i in range(1, 5) if len(m[i]) in [2, 3, 4, 7])
    
    print(count)