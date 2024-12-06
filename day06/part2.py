import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def get_valid_invalid_positions(input_file):
    open = set()
    blocked = set()
    for y, line in enumerate(input_file):
        for x, char in enumerate(line):
            if char == '.':
                open.add((x, y))
            elif char == '#':
                blocked.add((x, y))
            else:
                open.add((x, y))
                start = (x, y)
                
    return start, open, blocked
    
def rotate(direction):
    return (-direction[1], direction[0])

def add(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def move(current_pos, open, blocked, direction):
    visited = {current_pos}
    while True:
        next_pos = add(current_pos, direction)
        if next_pos in open:
            current_pos = next_pos
            visited.add(next_pos)
        elif next_pos in blocked:
            direction = rotate(direction)
        else:
            return visited
        
def check_path(current_pos, open, blocked, direction):
    visited_state = {(current_pos, direction)}
    while True:
        next_pos = add(current_pos, direction)
        if (next_pos, direction) in visited_state:
            return True
        elif next_pos in open:
            current_pos = next_pos
            visited_state.add((next_pos, direction))
        elif next_pos in blocked:
            direction = rotate(direction)
        else:
            return False

def main():
    input_file = get_input()
    start_pos, open, blocked = get_valid_invalid_positions(input_file)
    visited = move(start_pos, open, blocked, (0, -1))
    total = 0
    for cell in visited.difference({start_pos}):
        total += check_path(start_pos, open.difference({cell}), blocked.union({cell}), (0, -1))
    print(total)
    
    


if __name__ == "__main__":
    main()