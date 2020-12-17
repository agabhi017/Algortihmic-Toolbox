import os
import numpy as np

def binary_search_recursion(numbers, key, l, r) :
    if l > r :
        return -1
    
    m = int(np.floor(l + (r - l)/2))
    
    if key == numbers[m] :
        return m
       
    if key > numbers[m] :
        return binary_search_recursion(numbers, key, m + 1, r)
    else :
        return binary_search_recursion(numbers, key, l, m - 1)
        

def binary_search(array, keys) :
    len_array = array[0]
    numbers = array[1:]
    key_match = keys[1:]
    indices = []
    
    for key in key_match :
        index = binary_search_recursion(numbers, key, 0, len_array - 1)
        indices.append(index)
        
    return indices

if __name__ == "__main__" :
    array = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    print(*binary_search(array, keys))