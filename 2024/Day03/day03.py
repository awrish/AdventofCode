import os
import re

from collections import defaultdict
import math

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')


# re.findall()
def part1():
    text = ""

    for line in open(filename):
        text += line
    
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, text)
    
    numPattern = r"\d{1,3},\d{1,3}"

    ans = 0

    for match in matches:
        nums = re.findall(numPattern, match)
        for num in nums:
            num1, num2 = num.split(',')
            ans += int(num1) * int(num2)
            
        
    print(ans)

    # should split into different functions for better readability
    part2 = 0
    newPattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    newMatches = re.findall(newPattern, text)

    flag = True
    for match in newMatches:
        if match == "don't()":
            flag = False
        elif match == "do()":
            flag = True
        else:
            if flag == False:
                continue
            nums = re.findall(numPattern, match)
            for num in nums:
                num1, num2 = num.split(",")
                part2 += int(num1) * int(num2)
        
    print(part2)



def main():
    part1()

if __name__ == '__main__':
    main()
