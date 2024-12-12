import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_input(input):
    pos_map = {}
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            pos_map[x + y*1j] = char
    return pos_map

def get_edges(pos_map, max_x, max_y):
    edges = {}
    for x in range(max_x+1):
        for y in range(max_y+1):
            z = x+y*1j
            char = pos_map[z]
            edges[z] = set()
            if pos_map.get(z + 1, '') != char:
                edges[z].add((z+1, '|'))
            if pos_map.get(z + 1j, '') != char:
                edges[z].add((z+1j, '-'))
            if pos_map.get(z - 1, '') != char:
                edges[z].add((z, '|'))
            if pos_map.get(z - 1j, '') != char:
                edges[z].add((z, '-'))
    return edges
                
def get_areas(pos_map, remaining):
    areas = []
    while remaining:
        pos_queue = [remaining.pop()]
        current_area = set()
        while pos_queue:
            current_pos = pos_queue[0]
            del pos_queue[0]
            current_area.add(current_pos)
            char = pos_map[current_pos]
            for direction in (1, -1, 1j, -1j):
                new_pos = current_pos + direction
                if pos_map.get(new_pos, '') == char and new_pos in remaining:
                    pos_queue.append(new_pos)
                    remaining.remove(new_pos)
        areas.append(current_area)      
    return areas    
             
def get_sides(edges):
    remaining = set(edges)
    num_sides = 0
    while remaining:
        start_edge = remaining.pop()
        if start_edge[1] == '-':
            current_pos = start_edge[0]
            while True: # Search right
                rightwards_corners = {(z, '|') for z in [current_pos+1, current_pos+1-1j]}
                remaining.discard((current_pos, '-'))
                if rightwards_corners.intersection(edges):
                    break
                current_pos += 1
                
            current_pos = start_edge[0]
            while True: # Search left
                leftwards_corners = {(z, '|') for z in [current_pos, current_pos-1j]}
                remaining.discard((current_pos, '-'))
                if leftwards_corners.intersection(edges):
                    break
                current_pos -= 1
        else:
            current_pos = start_edge[0]
            while True: # Search up
                upwards_corners = {(z, '-') for z in [current_pos-1, current_pos]}
                remaining.discard((current_pos, '|'))
                if upwards_corners.intersection(edges):
                    break
                current_pos -= 1j
                
            current_pos = start_edge[0]
            while True: # Search down
                downwards_corners = {(z, '-') for z in [current_pos-1+1j, current_pos+1j]}
                remaining.discard((current_pos, '|'))
                if downwards_corners.intersection(edges):
                    break
                current_pos += 1j
        num_sides += 1
    return num_sides
            

def main():
    input_file = get_input()
    pos_map = parse_input(input_file)
    max_x = len(input_file[0]) - 1
    max_y = len(input_file) - 1
    
    edges = get_edges(pos_map, max_x, max_y)
    areas = get_areas(pos_map, set(pos_map.keys()))
    
    total = 0
    for area in areas:
        area_edges = set.union(*[edges[pos] for pos in area])
        total += get_sides(area_edges) * len(area)
    print(total)


if __name__ == "__main__":
    main()