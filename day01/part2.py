import os
from collections import defaultdict

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def main():
    input_file = get_input()
    left_nums = []
    right_count = defaultdict(lambda: 0)
    for line in input_file:
        val1, val2 = line.split('   ')
        left_nums.append(int(val1))
        right_count[int(val2)] += 1
        
    total = 0
    for num in left_nums:
        total += num * right_count[num]
        
    print(total)


if __name__ == "__main__":
    main()