import os
from collections import defaultdict

# Topological sort may be relevant if there's a harder version of todays problem

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n\n')
    return input_file


def order_list(lt_map, nums):
    class PageNumber:
        def __init__(self, num):
            self.num = num
            
        def __lt__(self, other):
            return other.num in lt_map[self.num]
        
    page_nums = [PageNumber(num) for num in nums]
    page_nums.sort()
    return page_nums[len(nums)//2].num
    

def eval_list(lt_map, nums):
    for i in range(len(nums) - 1):
        if nums[i+1] not in lt_map[nums[i]]:
            return order_list(lt_map, nums)
    return 0

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