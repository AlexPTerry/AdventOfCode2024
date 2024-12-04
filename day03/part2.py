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

def find_next_do(text):
    return text.find("do()")

def find_next_dont(text):
    index = text.find("don't()")
    if index == -1:
        return len(text)
    return text.find("don't()")

def main():
    input_file = get_input()
    
    total = 0
    text = input_file
    on = True
    
    while text:
        if on:
            off_from = find_next_dont(text)
            start, end = (text[:off_from], text[off_from + 7:])
            total += calc_multiples(start)
            text = end
            on = False
        else:
            on_from = find_next_do(text)
            if on_from == -1:
                break
            text = text[on_from + 4:]
            on = True
            
    print(total)
            
            
            
            
    

if __name__ == "__main__":
    main()