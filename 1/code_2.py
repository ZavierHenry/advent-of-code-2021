import requests
from queue import Queue





if __name__ == "__main__":
    count = 0
    window = Queue()
    filename = "advent_day_1_input.txt"

    with open(filename, 'r') as reader:
        for i in range(3):
            value = int(reader.readline())
            window.put(value)
        
        for line in reader:
            value = int(line)
            front = window.get()
            if value > front:
                count += 1
            
            window.put(value)
    
    print(count)
            

