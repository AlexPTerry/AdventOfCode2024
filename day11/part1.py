import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip()
    return input_file

def calc_stones(number, steps, memory):
    if steps == 0:
        return 1
    
    if (number, steps) in memory:
        return memory[(number, steps)]
    
    str_number = str(number)
    if number == 0:
        subtotal = calc_stones(1, steps - 1, memory)
    elif len(str_number) % 2 == 0:
        subtotal = (calc_stones(int(str_number[:len(str_number)//2]), steps - 1, memory) + 
                    calc_stones(int(str_number[len(str_number)//2:]), steps - 1, memory))
    else:
        subtotal = calc_stones(number * 2024, steps - 1, memory)
    memory[(number, steps)] = subtotal
    return subtotal


def main():
    input_file = get_input()
    
    total = 0
    steps = 25
    memory = {}
    for number in [int(num) for num in input_file.split(' ')]:
        total += calc_stones(number, steps, memory)
        
    print(total)


if __name__ == "__main__":
    main()