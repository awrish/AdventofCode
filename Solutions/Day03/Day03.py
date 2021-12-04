import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'input.txt')

def main():
    with open(filename) as f:
        contents = f.read()
        count = 0
        answer = []
        eps = []
        while count != 12:
            counter1 = 0
            counter0 = 0
            for line in contents.splitlines():            
                print(line[count])
                found = int(line[count])
                if (found == 1):
                    counter1 += 1
                elif (found == 0):
                    counter0 += 1
            #print('Number of 1: ',counter1, '\nNumber of 0: ', counter0)
            if (counter1 > counter0):
                answer.append(1)
                eps.append(0)
            else:
                answer.append(0)
                eps.append(1)
            count += 1
        print('answer = ', answer)
        testing = ""
        epsString = ""
        for i in range(len(answer)):
            testing += str(answer[i])
        for i in range(len(eps)):
            epsString += str(eps[i])
        
        final = int(testing,2) * int(epsString,2)
        print('testing: ', testing) #the binary string that is the result
        print('resut: ', int(testing,2)) #converts the binary string to base 10
        print('final: ', final)


        #part two
        count = 0
        oxygen = contents.splitlines()
        while (len(oxygen) > 1):
            ones = []
            zeros = []
            for i in range(len(oxygen)):
                if (oxygen[i][count]) == '1':
                    ones.append(oxygen[i])
                else:
                    zeros.append(oxygen[i])
            
            oxygen = [zeros,ones][len(ones) >= len(zeros)]
            count += 1
        oxy = "".join(*oxygen)

        co2 = contents.splitlines()
        count = 0
        while(len(co2) > 1):
            cOnes = []
            cZeros = []
            for i in range(len(co2)):
                if (co2[i][count] == '1'):
                    cOnes.append(co2[i])
                else:
                    cZeros.append(co2[i])
                
            co2 = [cZeros,cOnes][len(cOnes) < len(cZeros)]
            count += 1
        numCo = "".join(*co2)

        print('final ans = ', int(oxy,2) * int(numCo,2))

if __name__ == '__main__':
    main()