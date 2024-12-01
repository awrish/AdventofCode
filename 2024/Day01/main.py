# sort both lists and pair them, find diff between all pairs

# O(N log N)

import os
from collections import defaultdict

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')




def day1():
    
    with open(filename) as f:
        lines = f.read().splitlines()
    col1, col2 = [], []

    for line in lines:
        num1, num2 = line.split()

        col1.append(int(num1))
        col2.append(int(num2))
    
    res = 0

    for n1, n2 in zip(sorted(col1), sorted(col2)):
        res += abs(n2 - n1)
    

    # using hashmap instead of counter
    freqMap = defaultdict(list)

    for num in col2:
        freqMap[num] = freqMap.get(num, 0) + 1
    
    simScore = 0

    for num in col1:
        if num in freqMap:
            simScore += num * freqMap[num]
    
    print(simScore)


    


day1()






