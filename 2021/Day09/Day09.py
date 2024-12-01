#DFS might be a good approach
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')

def main():
    with open(filename) as f:
        contents = f.read()
        print(contents)

main()
