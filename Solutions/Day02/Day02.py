import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')

def main():
    vertical = 0
    horizontal = 0    
    aim = 0 #part 3
    with open(filename) as f:
        contents = f.read()
        for line in contents.splitlines():
            splitter = line.split(" ")
            direction = splitter[0]
            change = int(splitter[1])
            if (direction == 'up'):
               # vertical -= change
                aim -= change #part 3
            elif direction == 'down':
               # vertical += change
                aim += change
            elif direction == 'forward':
                horizontal += change
                vertical += aim * change #part3

    #total = horizontal * vertical
    total = horizontal * vertical
    print('total: ', total)


if __name__ == '__main__':
    main()