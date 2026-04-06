import sys
from highestValSubsequence import highestVal
from backtracking import backtrack
from verification import verify

'''
Input Format
The input is given in the following format:
K
x1 v1
x2 v2
...
xK vK
A
B

• K is the number of characters in the alphabet.
• Each of the next K lines contains a character and its value.
• A is the first string.
• B is the second string.
'''


def main():
    # parse input from example1.in
    if len(sys.argv) < 2:
        print("No input file specified.")
        print("Command line format: python main.py <input_file_path> [output_file_path]")
        print("Example: python main.py data/example1.in data/example.out")
        exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else None

    if len(sys.argv) < 2:
        print("No input file specified.")
        print("Command line format: python main.py <input_file_path> [output_file_path]")
        print("Example: python main.py data/example1.in data/example.out")
        exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        # open file for command line input and read lines into a list of strings
        with open(input_file_path, 'r') as f:
            lines = [l.strip() for l in f.readlines()]

        # get the total number of letters in the alphabet
        k = int(lines[0])

        # read in the alphabet
        alphabet = {}
        for i in range(1, k + 1):
            # split letter, value based on spaces into a list and map to string types
            letter_value = list(map(str, lines[i].split()))
            alphabet[letter_value[0]] = int(letter_value[1])

        A = lines[k + 1]
        B = lines[k + 2]

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == '__main__':
    main()