import numpy as np

def knapsack_gold(w, items) :
    n_items = len(items)
    array = np.zeros((n_items + 1, w + 1), dtype = int)
    for i in range(1, n_items + 1) :
        for j in range(1, w + 1) :
            if items[i - 1] <= j :
                array[i][j] = max(array[i - 1][j - items[i - 1]] + items[i - 1], array[i - 1][j])
            else :
                array[i][j] = array[i - 1][j]
    return array[n_items][w]

if __name__ == "__main__" :
    input_1 = list(map(int, input().split()))
    w = input_1[0]
    items = list(map(int, input().split()))
    print(knapsack_gold(w, items))