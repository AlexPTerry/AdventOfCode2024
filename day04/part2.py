import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def parse_input_file(input_file):
    position_dict = {}
    a_char_list = []
    for y, line in enumerate(input_file):
        for x, char in enumerate(line):
            position_dict[(x, y)] = char
            if char == 'A':
                a_char_list.append((x,y))
    return position_dict, a_char_list
            
def mult_tuple(mul, tup):
    return (mul*tup[0], mul*tup[1])

def add_tuples(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])
            
def eval_pos(pos, position_dict):
    directions = [(i, j) for i in (-1, 1) for j in (-1, 1)]
    
    pos_m1_m1 = position_dict.get(add_tuples(pos,(-1,-1)), "")
    pos_p1_p1 = position_dict.get(add_tuples(pos,(1,1)), "")
    pos_m1_p1 = position_dict.get(add_tuples(pos,(-1,1)), "")
    pos_p1_m1 = position_dict.get(add_tuples(pos,(1,-1)), "")

    if (pos_m1_m1 in {"M", "S"} and
        pos_p1_p1 in {"M", "S"} and pos_p1_p1!= pos_m1_m1 and
        pos_m1_p1 in {"M", "S"} and
        pos_p1_m1 in {"M", "S"} and pos_p1_m1!= pos_m1_p1):
        return 1
    return 0
              

def main():
    input_file = get_input()
    position_dict, a_char_list = parse_input_file(input_file)
    
    total = 0
    for pos in a_char_list:
        total += eval_pos(pos, position_dict)
    
    print(total)
    
    


if __name__ == "__main__":
    main()