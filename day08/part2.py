import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_input(input_file):
    valid_positions = set()
    antennae = {}
    for y, line in enumerate(input_file):
        for x, char in enumerate(line):
            pos = (x, y)
            valid_positions.add(pos)
            if char == '.':
                continue
            if char not in antennae:
                antennae[char] = set()
            antennae[char].add(pos)
    max_x = len(input_file[0]) - 1
    max_y = len(input_file) - 1
    return valid_positions, antennae, max_x, max_y

def get_locations(antenna_positions, valid_positions, max_x, max_y):
    pairs = [(e1, e2) for e1 in antenna_positions for e2 in antenna_positions if e1 != e2]
    antinodes = set()
    for pair in pairs:
        antinodes.update(get_pair_locations(pair, max_x, max_y))
    return antinodes.intersection(valid_positions)

def is_valid(location, max_x, max_y):
    return 0 <= location[0] <= max_x and 0 <= location[1] <= max_y

def get_pair_locations(pair, max_x, max_y):
    p1, p2 = pair
    diff = (p2[0] - p1[0], p2[1] - p1[1])
    pair_locations = set()
    
    new_location = (p1[0], p1[1])
    while is_valid(new_location, max_x, max_y):
        pair_locations.add(new_location)
        new_location = (new_location[0] - diff[0], new_location[1] - diff[1])
        
    new_location = (p2[0], p2[1])
    while is_valid(new_location, max_x, max_y):
        pair_locations.add(new_location)
        new_location = (new_location[0] + diff[0], new_location[1] + diff[1])
        
    return pair_locations

def main():
    input_file = get_input()
    valid_positions, antennae, max_x, max_y = parse_input(input_file)
    antinode_locations = set()
    
    for antenna in antennae:
        antinode_locations.update(get_locations(antennae[antenna], valid_positions, max_x, max_y))
        
    print(len(antinode_locations))


if __name__ == "__main__":
    main()