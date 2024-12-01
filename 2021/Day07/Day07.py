#maybe create a hashmap and add all unique digits in position
#scan through hashmap and subtract the values from hashmap and += a holder value
#have a min value and if holder is < min min is equal to holder and ans is equal to that value in the hashmap

import os
import math

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')

def testing():
    with open(filename) as f:
        contents = f.read()
        position = {}
        holder = float('inf')
        answer = 0
        #print('len: ', len(contents))

        for i in range(0, len(contents)):
            for num in range(0, len(contents)):
                if not position.get(num):
                    position[num] = []
                position[num].append(abs(i-num))
        for i, j in position.items():
            if sum(j) < holder:
                holder = sum(j)
        print('answer', holder)

                

testing()
