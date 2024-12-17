import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def get_combo(registers, combo):
    if combo <= 3:
        return combo
    elif combo == 4:
        return registers['A']
    elif combo == 5:
        return registers['B']
    elif combo == 6:
        return registers['C']

def adv(registers, combo):
    registers['A'] >>= get_combo(registers, combo)

def bxl(registers, literal):
    registers['B'] ^= literal
    
def bst(registers, combo):
    registers['B'] = get_combo(registers, combo) & 7
    
def jnz(registers, literal):
    if registers['A'] != 0:
        registers['P'] = literal
        registers['P'] -= 2 # Counteract pointer increase if jump occurs
        
def bxc(registers, _):
    registers['B'] ^= registers['C']
    
def out(registers, combo):
    registers['O'] = get_combo(registers, combo) & 7
    
def bdv(registers, combo):
    registers['B'] = registers['A'] >> get_combo(registers, combo)
    
def cdv(registers, combo):
    registers['C'] = registers['A'] >> get_combo(registers, combo)

def run_program(A_val, program, opcodes):
    registers = {
        'A': A_val,
        'B': 0,
        'C': 0,
        'P': 0,
        'O': -1
    }
    while registers['P'] < len(program):
        opcode = program[registers['P']]
        operand = program[registers['P'] + 1]
        opcodes[opcode](registers, operand)
        registers['P'] += 2
    return registers['O']

def check_As(A_vals, expected_out, program, opcodes):
    next_As = []
    for A_val in A_vals:
        shifted = A_val << 3
        for i in range(8):
            A_potential = shifted + i
            out = run_program(A_potential, program, opcodes)
            if out == expected_out:
                next_As.append(A_potential)
    return next_As

def main():
    input_file = get_input()
    program_string = input_file[4].split(": ")[1]
    program = list(map(int, program_string.split(",")))
    opcodes = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }
    
    potential_As = [0]
    for num in program[::-1]:
        potential_As = check_As(potential_As, num, program[:-2], opcodes)
    print(sorted(potential_As)[0])
    

if __name__ == "__main__":
    main()