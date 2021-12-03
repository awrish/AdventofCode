import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')

def main():
    with open(filename) as f:
        w = [int(x) for x in next(f).split()]
        array = []
        for line in f:
            array.append([int(x) for x in line.split()])
        #print('the array is: ', array)
        amount = 0
        for i in range(len(array)):
            if array[i] > array[i-1]:
                amount += 1
        print('the amount is: ', amount)

        #for part 2
        print('the total for the sliding window is: ', sum(x < y for x,y in zip(array, array[3:])))

            

# Tests against smaller example to get 
# it right before moving into the larger
# input
def test(arr):
    count = 0
    print(' this is the array: ', arr)
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            count += 1
    print('count should be equal to 7')
    print('the count is: ' , count)
 


arr2 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
if __name__ == '__main__':
    main()
   # test(arr2)
