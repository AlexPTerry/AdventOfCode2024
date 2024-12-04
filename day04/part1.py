import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_input_file(input_file):
    position_dict = {}
    x_char_list = []
    for y, line in enumerate(input_file):
        for x, char in enumerate(line):
            position_dict[(x, y)] = char
            if char == 'X':
                x_char_list.append((x,y))
    return position_dict, x_char_list
            
def mult_tuple(mul, tup):
    return (mul*tup[0], mul*tup[1])

def add_tuples(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])
            
def eval_pos(pos, position_dict):
    directions = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i==0 and j==0)]
    xmas = "XMAS"
    total = 0
    for direction in directions:
        add = 1
        for i in range(1, len(xmas)):
            if position_dict.get(add_tuples(pos, mult_tuple(i, direction)), "") != xmas[i]:
                add = 0
                break
        total += add
            
    return total
              

def main():
    input_file = get_input()
    position_dict, x_char_list = parse_input_file(input_file)
    
    total = 0
    for pos in x_char_list:
        total += eval_pos(pos, position_dict)
    
    print(total)
    
    


if __name__ == "__main__":
    main()