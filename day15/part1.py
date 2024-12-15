import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n\n')
    return input_file

def parse_grid(grid):
    walls = set()
    boxes = set()
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '@':
                start = x + y*1j
            elif char == '#':
                walls.add(x + y*1j)
            elif char == 'O':
                boxes.add(x + y*1j)
    return start, walls, boxes

def parse_input(input):
    start, walls, boxes = parse_grid(input[0].split('\n'))
    directions = input[1].replace("\n", "")
    return start, walls, boxes, directions

def box_move(box, direction, boxes, walls):
    target = box + direction
    if target in walls:
        return False
    if target in boxes:
        if not box_move(target, direction, boxes, walls):
            return False
    boxes.remove(box)
    boxes.add(target) # Should only really be removing/adding boxes at the start/end
    return True

def move(current_pos, direction, walls, boxes):
    target = current_pos + direction
    if target in walls:
        return current_pos, boxes
    if target in boxes:
        if box_move(target, direction, boxes, walls):
            return target, boxes
        return current_pos, boxes
    return target, boxes

def main():
    input_file = get_input()
    current_pos, walls, boxes, directions = parse_input(input_file)
    
    direction_dict = {
        '^': -1j,
        '>': 1,
        'v': 1j,
        '<': -1
    }
    for direction in directions:
        current_pos, boxes = move(current_pos, direction_dict[direction], walls, boxes)
        
    total = 0
    for box in boxes:
        total += int(box.real + 100*box.imag)
    print(total)


if __name__ == "__main__":
    main()