import os
import numpy as np
from collections import deque

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')

#another func to check if it is a winning board
def is_winning_board(board): 
    #something here
    print(board)


def solution():
    #main function
    with open(filename) as f:
        contents = f.read()
        print(contents)



def testing():
    print("This is a pretty good keyboard mane!!!")

testing()



#Pretty tough --> Gonna do it later

solution()