import numpy as np

def edit_distance(a,b) :
    len_a = len(a)
    len_b = len(b)
    dist_matrix = np.zeros((len_a + 1, len_b + 1), dtype = int)
    for i in range(len_a + 1) :
        dist_matrix[i][0] = i
    for j in range(len_b + 1) :
        dist_matrix[0][j] = j
    
    for i in range(1, len_a + 1) :
        for j in range(1, len_b + 1) :
            if a[i - 1] == b[j - 1] :
                diff = 0
            else:
                diff = 1
            dist_matrix[i][j] = min((dist_matrix[i - 1][j] + 1), (dist_matrix[i][j - 1] + 1), (dist_matrix[i - 1][j - 1] + diff))

    return dist_matrix[len_a][len_b]

if __name__ == "__main__" :
    a = input()
    b = input()
    print(edit_distance(a,b))