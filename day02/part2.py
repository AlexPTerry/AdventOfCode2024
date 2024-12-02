import os
import numpy as np

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def is_safe(line):
    nums = np.asarray(list(map(int, line.split(' '))))
    for i in range(len(nums)): # Removing no number is safe => removing the first number is safe
        diff = np.diff(nums[np.arange(len(nums)) != i])
        if (np.all(diff >= 1) and np.all(diff <= 3) or np.all(diff <= -1) and np.all(diff >= -3)):
            return True
    return False

def main():
    input_file = get_input()
    
    total_safe = 0
    for line in input_file:
        if is_safe(line):
            total_safe += 1
            
    print(total_safe)


if __name__ == "__main__":
    main()