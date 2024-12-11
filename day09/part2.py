import os
from copy import copy

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip()
    return input_file
    
        
def calc_range(head, tail):
    return ((tail - 1)*tail - (head - 1)*head) // 2

def main():
    input_file = get_input()
    numbers = []
    sequence = []
    
    for i, char in enumerate(input_file):
        if i % 2 == 0:
            numbers.append([i//2, int(char)])
            sequence.append([i//2, int(char)])
        else:
            sequence.append([-1, int(char)])
            
    pointer = 0
    offset = len(sequence) % 2 == 0
    while True:
        if pointer >= len(sequence):
            break
        seq = sequence[pointer]
        if seq[0] != -1 or seq[1] == 0:
            pointer += 1
            continue
        
        for i in range(-1-offset, -len(sequence) + pointer, -2):
            if sequence[i][0] == -1:
                continue
            number = copy(sequence[i])
            if number[1] > seq[1]:
                continue
            seq[1] -= number[1]
            sequence[i] = [-1, number[1]]
            sequence.insert(pointer, number)
            break
        pointer += 1
    
    head = 0
    tail = 0
    total = 0
    for block in sequence:
        head = tail
        tail += block[1]
        if block[0] == -1 or block[1] == 0:
            continue
        total += block[0] * calc_range(head, tail)
    print(total)
            
        
            
        


if __name__ == "__main__":
    main()