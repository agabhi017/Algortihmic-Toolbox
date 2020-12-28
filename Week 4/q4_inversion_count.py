import os
import numpy as np

def naive_inversion_count(array, n) :
    count = 0
    for i in range(0, n) :
        for j in range(i + 1, n) :
            if array[j] < array[i]:
                count += 1

    return count

def merge(a,b, count) :
    array = []
    while len(a) > 0 and len(b) > 0 :
        
        if a[0] <= b[0] :
            array.append(a[0])
            a.remove(a[0])
        else :
            array.append(b[0])
            b.remove(b[0])
            count += len(a)
    
    if len(a) > 0 :
        for item in a :
            array.append(item)
    
    if len(b) > 0 :
        for item in b :
            array.append(item)
            
    return array, count

def merge_sort_count(array, left, right, count) :
    if left == right :
        return [array[left]], count
    m = int(np.floor(left + (right - left)/2))
    a, count = merge_sort_count(array, left, m, count)
    b, count = merge_sort_count(array, m + 1, right, count)
    return merge(a, b, count)

def merge_sort_inversion_count(array, n) :
    count = 0
    array, count = merge_sort_count(array, 0, n - 1, count)
    return count

if __name__ == "__main__" :
    n = int(input())
    array = list(map(int, input().split()))
    print(merge_sort_inversion_count(array, n))