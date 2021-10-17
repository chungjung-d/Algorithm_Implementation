import sys

def maxScore(nums):
    num_array = [1] + nums + [1]

    array_length = len(num_array)-1

    DT = [[0]*array_length for _ in range(array_length)]

    for L in range(1,array_length):
        for i in range(0,array_length-L):
            j = i + L
            
            max_num = -1

            for k in range(i,j):
                count = DT[i][k] + DT[k+1][j] + num_array[i]*num_array[j+1]*num_array[k+1]
                if(count > max_num):
                    max_num = count
                    DT[i][j] = count
    
    print(DT[0][array_length-1])

