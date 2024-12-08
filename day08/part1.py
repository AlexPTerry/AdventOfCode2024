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
    return valid_positions, antennae

def get_pair_locations(pair):
    p1, p2 = pair
    return {
        (2*p1[0] - p2[0], 2*p1[1] - p2[1]),
        (2*p2[0] - p1[0], 2*p2[1] - p1[1])
    }

def get_locations(antenna_positions, valid_positions):
    pairs = [(e1, e2) for e1 in antenna_positions for e2 in antenna_positions if e1 != e2]
    antinodes = set()
    for pair in pairs:
        antinodes.update(get_pair_locations(pair))
    return antinodes.intersection(valid_positions)

def main():
    input_file = get_input()
    valid_positions, antennae = parse_input(input_file)
    antinode_locations = set()
    
    for antenna in antennae:
        antinode_locations.update(get_locations(antennae[antenna], valid_positions))
        
    print(len(antinode_locations))


if __name__ == "__main__":
    main()