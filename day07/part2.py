import os
import operator as op

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def evaluate_line(nums, answer):
    if len(nums) == 1:
        return nums[0] == answer
    operators = [op.add, op.mul, lambda x, y: int(str(x)+str(y))]
    partials = [operator(*nums[:2]) for operator in operators]
    return any(map(lambda x: evaluate_line([x] + nums[2:], answer), partials))
        

def main():
    input_file = get_input()
    
    total = 0
    for i, line in enumerate(input_file):
        answer, nums = line.split(": ")
        nums = [int(num) for num in nums.split(" ")]
        answer = int(answer)
        if evaluate_line(nums, answer):
            total += answer
        
    print(total)
        
    
    


if __name__ == "__main__":
    main()