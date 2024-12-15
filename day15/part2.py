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
                start = 2*x + y*1j
            elif char == '#':
                walls.add(2*x + y*1j)
            elif char == 'O':
                boxes.add(2*x + y*1j)
    return start, walls, boxes

def parse_input(input):
    start, walls, boxes = parse_grid(input[0].split('\n'))
    directions = input[1].replace("\n", "")
    return start, walls, boxes, directions


def box_move_vert(box, direction, boxes, walls, moving_boxes):
    target = box + direction
    for offset in (-1, 0, 1):
        if target + offset in walls:
            return False
        
    for offset in (-1, 0, 1):
        if target in walls:
            return False
        if target + offset in boxes:
            if not box_move_vert(target + offset, direction, boxes, walls, moving_boxes):
                return False
    moving_boxes.add(box)
    return True

def box_move_left(box, boxes, walls, moving_boxes):
    target = box - 2
    if target in walls:
        return False
    if target in boxes:
        if not box_move_left(target, boxes, walls, moving_boxes):
            return False
    moving_boxes.add(box)
    return True

def box_move_right(box, boxes, walls, moving_boxes):
    target = box + 2
    if target in walls:
        return False
    if target in boxes:
        if not box_move_right(target, boxes, walls, moving_boxes):
            return False
    moving_boxes.add(box)
    return True

def move(current_pos, direction, walls, boxes):
    if direction.real == 0:
        target = current_pos + direction
        alt_target = target - 1
        if target in walls or alt_target in walls:
            return current_pos, boxes
        if target in boxes:
            moving_boxes = set()
            if box_move_vert(target, direction, boxes, walls, moving_boxes):
                new_boxes = set(box + direction for box in moving_boxes)
                boxes = boxes - moving_boxes
                boxes.update(new_boxes)
                return target, boxes
            return current_pos, boxes
        if alt_target in boxes:
            moving_boxes = set()
            if box_move_vert(alt_target, direction, boxes, walls, moving_boxes):
                new_boxes = set(box + direction for box in moving_boxes)
                boxes = boxes - moving_boxes
                boxes.update(new_boxes)
                return target, boxes
            return current_pos, boxes
    elif direction.real == 1:
        target = current_pos + 1
        if target in walls:
            return current_pos, boxes
        if target in boxes:
            moving_boxes = set()
            if box_move_right(target, boxes, walls, moving_boxes):
                new_boxes = set(box + direction for box in moving_boxes)
                boxes = boxes - moving_boxes
                boxes.update(new_boxes)
                return target, boxes
            return current_pos, boxes
    elif direction.real == -1:
        target = current_pos - 2
        if target in walls:
            return current_pos, boxes
        if target in boxes:
            moving_boxes = set()
            if box_move_left(target, boxes, walls, moving_boxes):
                new_boxes = set(box + direction for box in moving_boxes)
                boxes = boxes - moving_boxes
                boxes.update(new_boxes)
                return current_pos - 1, boxes
            return current_pos, boxes
        
    return current_pos + direction, boxes

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