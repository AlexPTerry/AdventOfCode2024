import os
from collections import deque

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_input(input, n_blocks, max_val):
    blocks = set(x + y*1j for x, y in [tuple(map(int, line.split(","))) for line in input[:n_blocks]])
    traversable = set(x + y*1j for x in range(max_val+1) for y in range(max_val+1) if x + y*1j not in blocks)
    return traversable

def traverse(start, end, traversable):
    queue = deque([(0, start)])
    traversable.remove(start)
    depth, pos = queue[0]
    while pos != end:
        depth, pos = queue.popleft()
        for direction in (1, 1j, -1, -1j):
            target = pos + direction
            if target not in traversable:
                continue
            traversable.remove(target)
            queue.append((depth + 1, target))
    return depth
        

def main():
    input_file = get_input()
    max_val = 70
    n_blocks = 1024
    start = 0
    end = max_val + max_val*1j
    traversable = parse_input(input_file, n_blocks, max_val)
    print(traverse(start, end, traversable))


if __name__ == "__main__":
    main()