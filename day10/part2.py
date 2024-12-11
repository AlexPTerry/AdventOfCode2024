import os

from copy import copy

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def add(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def parse_input(input):
    trailheads = []
    heights = {}
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            heights[(x, y)] = int(char)
            if char == '0':
                trailheads.append((x, y))
    return trailheads, heights
    
def traverse(position, height, heights):
    if position not in heights or (heights[position] - height) != 1:
        return 0
    if heights[position] == 9:
        return 1
    
    return sum(traverse(add(position, direction), 
                        heights[position], 
                        heights) for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)])

def main():
    input_file = get_input()
    trailheads, heights = parse_input(input_file)
    total = 0
    for trailhead in trailheads:
        subtotal = traverse(trailhead, -1, heights)
        total += subtotal
    print(total)


if __name__ == "__main__":
    main()