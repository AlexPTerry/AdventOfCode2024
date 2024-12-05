import os
from collections import defaultdict

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n\n')
    return input_file

def eval_list(lt_map, nums):
    for i in range(len(nums) - 1):
        if nums[i+1] not in lt_map[nums[i]]:
            return 0
    return nums[len(nums)//2]

def main():
    orders, lists = get_input()
    lt_map = defaultdict(lambda: set())
    
    for order in orders.split('\n'):
        n1, n2 = order.split('|')
        lt_map[int(n1)].add(int(n2))
    
    total = 0
    for line in lists.split('\n'):
        total += eval_list(lt_map, list(map(int, line.split(','))))
    print(total)


if __name__ == "__main__":
    main()