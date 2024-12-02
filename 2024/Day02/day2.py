import os

from collections import defaultdict
import math

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')

def test():

    with open(filename) as f:
        reports = [list(map(int, line.split())) for line in f]


    def is_safe(report: list, ignore_idx: int) -> bool:
        desc, asc, prev = False, False, None

        for idx, level in enumerate(report):
            if idx == ignore_idx:
                continue

            if not prev:
                prev = level
                continue

            if prev < level:
                asc = True
            elif prev > level:
                desc = True

            if (prev == level) or abs(prev - level) > 3 or (asc and desc):
                return False

            prev = level
        return True


    print(sum(any(is_safe(report, i) for i in range(len(report))) for report in reports))

def part2():

    valid = [1, 2, 3]

    with open(filename) as f:
        lines = f.read().splitlines()
    
    res = 0
    testAns = 0


    # increasing remove max of the two
    # decreasing remove the min


    for line in lines:
        arr = list(line.split())
        
        # for increasing, if clause is violated, append the min of the 2 values
        
        # skip over unsafe values, add rest to stack. if len stack is within 1, valid else unvalid

        # check increasing, this can't handle case where you remove first element
        
        prev = int(arr[0])
        stack = [prev]
        
        test = [prev]

        for i in range(1, len(arr)):
            num = int(arr[i])

            print(prev, num, num - prev)

            if num <= prev or num - prev not in valid:
                test.pop()
            
            test.append(num)


            if num > prev and num - prev in valid:
                stack.append(num)
            
            prev = num
            
        print(stack)
        if (len(arr) - len(stack)) <= 1:
            res += 1
        
        if len(arr) - len(test) <= 1:
            testAns += 1
        

        

    
    # check decreasing values
    for line in lines:
        arr = list(line.split())

        prev = int(arr[0])

        stack = [prev]

        test = [prev]

        for i in range(1, len(arr)):
            num = int(arr[i])

            # print(prev, num, prev - num, 'decreasing')

            if num >= prev or prev - num not in valid:
                test.pop()

            test.append(num)
            
            if num < prev and prev - num in valid:
                stack.append(num)

            prev = num

        print(stack)
        if (len(arr) - len(stack)) <= 1:
            res += 1
        
        if len(arr) - len(test) <= 1:
            testAns += 1
    
    # 414 too low 421 too high not 417 or 419
    print('part2 answer: ', res, testAns)






def part1():
    valid = [1, 2, 3]

    # check if sorted, ascending or descending
    # check if absolute diff between any element is not in valid, then unsafe

    with open(filename) as f:
        lines = f.read().splitlines()
    
    res = 0
    ans = 0
    
    # loop for increasing, and a loop for decreasing
    for line in lines:

        arr = list(line.split())
        
        prev = int(arr[0])
        temp = 1

        stack = [prev]

        # check increasing
        for i in range(1, len(arr)):
            val = int(arr[i])

            if val <= prev or (val - prev) not in valid:
                temp = 0
            else:
                stack.append(val)
            
            prev = val
        
        res += temp
        if len(arr) - len(stack) <= 1:
            ans += 1
    
    # check decreasing
    for line in lines:
        arr = list(line.split())

        prev = int(arr[0])
        temp = 1

        stack = [prev]

        for i in range(1, len(arr)):
            val = int(arr[i])

            if val >= prev or (prev - val) not in valid:
                temp = 0
            else:
                stack.append(val)
            
            prev = val
        
        res += temp
        if len(arr) - len(stack) <= 1:
            ans += 1

    print('part1 answer: ', res)
    # print('part2 answer: ', ans) # 414 too low, 421 too high 418 correct

            
        
    
    

def main():
    part1()
    part2()
    test()

if __name__ == '__main__':
    main()