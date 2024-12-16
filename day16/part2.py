import os
import heapq as hq
from collections import defaultdict

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_grid(grid):
    traversable = set()
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '#':
                continue
            if char == 'S':
                start = ((x, y), (1, 0))
            elif char == 'E':
                end = (x, y)
            traversable.add((x, y))
    return start, end, traversable
                
def get_connections(traversable, current):
    connections = {}
    connections[(current[0], (current[1][1], -current[1][0]))] = 1000 # Rotate left
    connections[(current[0], (-current[1][1], current[1][0]))] = 1000 # Rotate right
    if (forward := (current[0][0] + current[1][0], current[0][1] + current[1][1])) in traversable:
        connections[(forward, current[1])] = 1
    return connections

def dijkstra(traversable, start, end_pos):
    queue = [(0, start)]
    current = queue[0]
    paths = defaultdict(lambda: set())
    distances = defaultdict(lambda: 9999999999)
    
    while len(queue) > 0:
        distance, current = hq.heappop(queue)
        if distance > distances[current]:
            continue
        connections = get_connections(traversable, current)
        for state, cost in connections.items():
            new_distance = distance + cost
            if new_distance > distances[state]:
                continue
            if new_distance == distances[state]:
                paths[state].add(current)
                continue
            paths[state].add(current)
            distances[state] = new_distance
            hq.heappush(queue, (new_distance, state))
            
    return paths, distances
    
def add_pos(paths, visited, state):
    visited.add(state)
    for next_state in paths[state]:
        if next_state not in visited:
            add_pos(paths, visited, next_state)

def main():
    input_file = get_input()
    start, end_pos, traversable = parse_grid(input_file)
    paths, distances = dijkstra(traversable, start, end_pos)
    valid_end_states = [(end_pos, (1, 0)), (end_pos, (0, 1)), (end_pos, (-1, 0)), (end_pos, (0, -1))]
    min_distance = min(distances[state] for state in valid_end_states)
    potential_end_states = [end_state for end_state in valid_end_states if distances[end_state]==min_distance]
    visited = set()
    
    for end_state in potential_end_states:
        add_pos(paths, visited, end_state)
    print(len(set(state[0] for state in visited)))
    
    


if __name__ == "__main__":
    main()