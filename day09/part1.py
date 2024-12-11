import os
from collections import deque

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip()
    return input_file



def get_front(n, numbers):
    if len(numbers) == 0:
        return []
    if n < numbers[0][1]:
        numbers[0][1] -= n
        return [(n, numbers[0][0])]
    elif n == numbers[0][1]:
        final_val = numbers[0][0]
        del numbers[0]
        return [(n, final_val)]
    else:
        num_end = numbers[0][1]
        final_val = numbers[0][0]
        del numbers[0]
        return [(num_end, final_val)] + get_front(n-num_end, numbers)

def get_back(n, numbers):
    if len(numbers) == 0:
        return []
    if n < numbers[-1][1]:
        numbers[-1][1] -= n
        return [(n, numbers[-1][0])]
    elif n == numbers[-1][1]:
        final_val = numbers[-1][0]
        del numbers[-1]
        return [(n, final_val)]
    else:
        num_end = numbers[-1][1]
        final_val = numbers[-1][0]
        del numbers[-1]
        return [(num_end, final_val)] + get_back(n-num_end, numbers)
    
    
    
def calc_total(head, tail, num_pairs, out):
    total = 0
    # print(head, tail, num_pairs)
    for pair in num_pairs:
        # print("    ", pair, calc_range(head, head+pair[0]), (head, head+pair[0]))
        total += pair[1] * calc_range(head, head+pair[0])
        head += pair[0]
        out += pair[0] * [pair[1]]
    return total
        
def calc_range(head, tail):
    return ((tail - 1)*tail - (head - 1)*head) // 2

def main():
    input_file = get_input()
    numbers = []
    spaces = []
    for i, char in enumerate(input_file):
        if i % 2 == 0:
            numbers.append([i//2, int(char)])
            
    head = 0
    tail = 0
    total = 0
    out = []
    
    for i, char in enumerate(input_file):
        head = tail
        tail += int(char) 
        # print("Total: ", total)
        # print(''.join([str(x) for x in out]))
        # print()
        if i % 2 == 0:
            num_pairs = get_front(tail - head, numbers)
            total += calc_total(head, tail, num_pairs, out)
        else:
            num_pairs = get_back(tail - head, numbers)
            total += calc_total(head, tail, num_pairs, out)
        if len(numbers) == 0:
            break
        
    # print(''.join([str(x) for x in out]))
    print(total)
            
        
            
        


if __name__ == "__main__":
    main()