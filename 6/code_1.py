global memory

def number_children(fish, days):
    if days < fish:
        return 0

    if (fish,days) in memory:
        return memory[(fish, days)]

    children = ((days - fish) // 7) + 1
    for x in range(days-fish, 0, -7):
        children += number_children(9, x)
        
    memory[(fish, days)] = children

    return children

if __name__ == "__main__":

    with open('input.txt', 'r') as reader:
        fish = [ int(x) + 1 for x in reader.read().strip().split(',') ]

    memory = {}

    fish_count = len(fish)
    for f in fish:
        children = number_children(f, 80)
        fish_count += children

    print(fish_count)
    
    