import os
import numpy as np

def partition_2part(array, left, right) :
    pivot = array[left]
    j = left
    for i in range(left + 1, right) :
        if array[i] <= pivot :
            j += 1
            array[j], array[i] = array[i], array[j]
    array[left], array[j] = array[j], array[left]
    return j
    
def partition_3part(array, left, right) :
    pivot = array[left]
    j = left
    count = 0
    
    for i in range(left + 1, right) :
        if array[i] < pivot :
            j += 1
            array[j], array[i] = array[i], array[j]
    array[left], array[j] = array[j], array[left]
    
    for i in range(left, right) :
        if array[i] == pivot and j > i :
            j = j - 1
            count += 1
            array[j], array[i] = array[i], array[j]
        elif array[i] == pivot and j < i :
            count += 1
            array[j + count], array[i] = array[i], array[j + count]
    return j, j + count

def randomized_quick_sort_2(array, left, right) :
    if left >= right :
        return
    pivot_index = np.random.choice(range(left, right))
    array[left], array[pivot_index] = array[pivot_index], array[left]
    m = partition_2part(array, left, right)
    randomized_quick_sort_2(array, left, m)
    randomized_quick_sort_2(array, m + 1, right)
    return array
    
def randomized_quick_sort_3(array, left, right) :
    if left >= right :
        return
    pivot_index = np.random.choice(range(left, right))
    array[left], array[pivot_index] = array[pivot_index], array[left]
    m, k = partition_3part(array, left, right)
    randomized_quick_sort_3(array, left, m)
    randomized_quick_sort_3(array, k + 1, right)
    return array

def quick_sort_2_part(array) :
    return randomized_quick_sort_2(array, 0, len(array))
    
def quick_sort_3_part(array) :
    return randomized_quick_sort_3(array, 0, len(array))

if __name__ == "__main__" :
    n = int(input())
    array = list(map(int, input().split()))
    print(*quick_sort_3_part(array))