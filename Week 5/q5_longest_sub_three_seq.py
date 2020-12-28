import numpy as np

def longest_sub_seq(a, b, c) :
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    array = np.zeros((len_a + 1, len_b + 1, len_c + 1), dtype = int)
    for i in range(1, len_a + 1) :
        for j in range(1, len_b + 1):
            for k in range(1, len_c + 1):
                if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1] :
                    array[i][j][k] = array[i - 1][j - 1][k - 1] + 1
                else:
                    array[i][j][k] = max(array[i - 1][j][k], array[i][j - 1][k], array[i][j][k - 1])
    return array[len_a][len_b][len_c]

if __name__ == "__main__" :
    p = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = list(map(int, input().split()))
    r = int(input())
    c = list(map(int, input().split()))
    print(longest_sub_seq(a, b, c))