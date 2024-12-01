import os

def get_input(name="input.dat"):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, name)
    with open(input_file_path, 'r') as file:
        input_file = file.read().strip().split('\n')
    return input_file

def main():
    input_file = get_input()
    l1 = []
    l2 = []
    for line in input_file:
        val1, val2 = line.split('   ')
        l1.append(int(val1))
        l2.append(int(val2))
        
    l1.sort()
    l2.sort()
    total = 0
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
        
    print(total)


if __name__ == "__main__":
    main()