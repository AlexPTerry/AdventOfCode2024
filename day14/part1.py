import os, re

from math import prod

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_input(input):
    out = []
    for line in input:
        temp = list(map(int, re.findall(r'\-?\d+', line)))
        out.append([(temp[0], temp[1]), (temp[2], temp[3])])
    return out

def add(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def mult(scalar, tup):
    return (scalar * tup[0], scalar * tup[1])

def mod(mod_tup, tup):
    return (tup[0] % mod_tup[0], tup[1] % mod_tup[1])

def calc_position(start, velocity, n_seconds, bounds):
    return mod(bounds, add(start, mult(n_seconds, velocity)))

def calc_quadrant(pos, bounds):
    mid_x = bounds[0] // 2
    mid_y = bounds[1] // 2
    
    if pos[0] == mid_x or pos[1] == mid_y:
        return -1
    return (1 if pos[0] > mid_x else 0) + 2 * (1 if pos[1] > mid_y else 0)

def calc_final_quadrants(robots, bounds, n_seconds):
    quadrants = [0] * 4
    for robot in robots:
        quadrant = calc_quadrant(calc_position(robot[0], robot[1], n_seconds, bounds), bounds)
        if quadrant == -1:
            continue
        quadrants[quadrant] += 1
    return quadrants

def main():
    input_file = get_input()
    robots = parse_input(input_file)
    # bounds = (11, 7)
    bounds = (101, 103)
    n_seconds = 100
    
    print(prod(calc_final_quadrants(robots, bounds, n_seconds)))


if __name__ == "__main__":
    main()