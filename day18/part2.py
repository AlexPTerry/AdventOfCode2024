import os
from collections import deque

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_input(input, max_val):
    blocks = [x + y*1j for x, y in [tuple(map(int, line.split(","))) for line in input]]
    traversable = set(x + y*1j for x in range(max_val+1) for y in range(max_val+1))
    return blocks, traversable

def is_traversable(start, end, traversable):
    queue = deque([(0, start)])
    visited = {start}
    depth, pos = queue[0]
    while queue:
        depth, pos = queue.popleft()
        for direction in (1, 1j, -1, -1j):
            target = pos + direction
            if target in visited or target not in traversable:
                continue
            visited.add(target)
            queue.append((depth + 1, target))
    return end in visited
        

def main():
    input_file = get_input()
    max_val = 70
    start = 0
    end = max_val + max_val*1j
    blocks, traversable = parse_input(input_file, max_val)
    traversable -= set(blocks)
    for block in reversed(blocks):
        traversable.add(block)
        if is_traversable(start, end, traversable):
            print(f"{int(block.real)},{int(block.imag)}")
            break


if __name__ == "__main__":
    main()