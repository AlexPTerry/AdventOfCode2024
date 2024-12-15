import os, re

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n\n')
    return input_file

def parse_block(block):
    lines = block.split('\n')
    parameters = {}
    parameters['a'] = tuple(map(int, re.findall(r'\d+', lines[0])))
    parameters['b'] = tuple(map(int, re.findall(r'\d+', lines[1])))
    parameters['end'] = tuple(map(int, re.findall(r'\d+', lines[2])))
    return parameters

def parse_input(input):
    out = []
    for block in input:
        out.append(parse_block(block))
    return out
    
def get_solution(a, b, det, end):
    return (b[1]*end[0]-b[0]*end[1])/det, (a[0]*end[1]-a[1]*end[0])/det
    
    
def get_min_tokens(parameters):
    a = parameters['a']
    b = parameters['b']
    end = parameters['end']
    
    det = a[0]*b[1] - a[1]*b[0]
    if det != 0:
        a_presses, b_presses = get_solution(a, b, det, end)
        if not (a_presses.is_integer() and b_presses.is_integer() and 
                a_presses >= 0 and b_presses >= 0):
            return 0
        else:
            return int(3*a_presses + b_presses)
    
    if not (a[0]/a[1] == b[0]/b[1] == end[0]/end[1]):
        return 0
    
    # Annoying case where there are infinite solutions
    return 0
    
    
def main():
    input_file = get_input()
    parameter_blocks = parse_input(input_file)
    
    
    tokens = 0
    for parameters in parameter_blocks:
        tokens += get_min_tokens(parameters)
    print(tokens)


if __name__ == "__main__":
    main()