import numpy as np

def longest_sub_seq(a,b) :
    len_a = len(a)
    len_b = len(b)
    array = np.zeros((len_a + 1, len_b + 1), dtype = int)
    for i in range(1, len_a + 1) :
        count = 0
        for j in range(1, len_b + 1) :
            if a[i - 1] == b[j - 1] :
                array[i][j] = array[i - 1][j - 1] + 1
            else :
                array[i][j] = max(array[i - 1][j], array[i][j - 1])
            
    return array[len_a][len_b]

if __name__ == "__main__" :
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    print(longest_sub_seq(a,b))