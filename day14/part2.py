import os, re

from math import prod
import matplotlib as plt

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

def square_dist(tup1, tup2):
    return (tup1[0]-tup2[0]) ** 2 + (tup1[1]-tup2[1]) ** 2

def calc_position(start, velocity, n_seconds, bounds):
    return (mod(bounds, add(start, mult(n_seconds, velocity))), velocity)

def calc_total_distance(robots):
    return sum(square_dist(robot1[0], robot2[0]) for robot1 in robots for robot2 in robots)
    
def print_graph(robots, n, bounds):
    final_positions = set([calc_position(robot[0], robot[1], n, bounds) for robot in robots])
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            if (x, y) in final_positions:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()

def main():
    input_file = get_input()
    robots = parse_input(input_file)
    # bounds = (11, 7)
    bounds = (101, 103)
    step_length = 1
    current_robots = robots
    distances = []
    for i in range(1000):
        if i % 10 == 0:
            print(f"{i}/{1000}")
        current_robots = [calc_position(robot[0], robot[1], step_length, bounds) for robot in current_robots]
        distances.append(calc_total_distance(robots))
    plt(distances)
    
    # print(prod(calc_final_quadrants(robots, bounds, n_seconds)))


if __name__ == "__main__":
    main()