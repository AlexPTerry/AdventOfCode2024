import os
import re

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip()
    return input_file

def calc_multiples(str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, str)
    return sum(int(x) * int(y) for x, y in matches)

def main():
    input_file = get_input()
    total = calc_multiples(input_file)
    print(total)
            
            
if __name__ == "__main__":
    main()