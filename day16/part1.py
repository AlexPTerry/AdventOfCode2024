import os
import heapq as hq

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
    visited = set()
    while current[0] != end_pos:
        distance, current = hq.heappop(queue)
        visited.add(current)
        connections = get_connections(traversable, current)
        for state, cost in connections.items():
            if state in visited:
                continue
            hq.heappush(queue, (distance + cost, state))
    return distance
    
    

def main():
    input_file = get_input()
    start, end_pos, traversable = parse_grid(input_file)
    print(dijkstra(traversable, start, end_pos))
    
    


if __name__ == "__main__":
    main()