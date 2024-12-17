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
    registers['O'] += f"{get_combo(registers, combo) & 7},"
    
def bdv(registers, combo):
    registers['B'] = registers['A'] >> get_combo(registers, combo)
    
def cdv(registers, combo):
    registers['C'] = registers['A'] >> get_combo(registers, combo)

def main():
    input_file = get_input()
    registers = {
        'A': int(input_file[0].split(": ")[1]),
        'B': int(input_file[1].split(": ")[1]),
        'C': int(input_file[2].split(": ")[1]),
        'P': 0,
        'O': ""
    }
    program = list(map(int, input_file[4].split(": ")[1].split(",")))
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
    while registers['P'] < len(program):
        opcode = program[registers['P']]
        operand = program[registers['P'] + 1]
        opcodes[opcode](registers, operand)
        registers['P'] += 2

    print(registers['O'][:-1])

if __name__ == "__main__":
    main()