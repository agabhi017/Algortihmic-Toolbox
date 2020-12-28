import os
import numpy as np

def overlap_count_naive(segments, points) :
    overlap = []
    
    for point in points :
        seg_count = 0
        for segment in segments :
            count = 0
            if point <= segment[1] and point >= segment[0]:
                count += 1
            
            if count == 1 :
                seg_count += 1
        overlap.append(seg_count)
    return overlap

def merge(a,b) :
    array = []
    while len(a) and len(b) > 0 :
        if a[0] <= b[0] :
            array.append(a[0])
            a.remove(a[0])
        else :
            array.append(b[0])
            b.remove(b[0])
        
    if len(a) > 0:
        for item in a :
            array.append(item)
    if len(b) > 0:
        for item in b :
            array.append(item)
    return array
    
def merge_sort(array, left, right) :
    if left == right :
        return [array[left]]
    m = int(np.floor(left + (right - left)/2))
    a = merge_sort(array, left, m)
    b = merge_sort(array, m + 1, right)
    return merge(a,b)

def merge_sort_modified(array, left, right) :
    if left == right :
        return [[array[0][left]], [array[1][left]]]
    m = int(np.floor(left + (right - left)/2))
    a = merge_sort_modified(array, left, m)
    b = merge_sort_modified(array, m + 1, right)
    return merge_modified(a,b)

def merge_modified(a, b) :
    array_l = []
    array_r = []
    while len(a[0]) > 0 and len(b[0]) > 0:
        if a[0][0] <= b[0][0]:
            array_l.append(a[0][0])
            array_r.append(a[1][0])
            a[0].remove(a[0][0])
            a[1].remove(a[1][0])
        else :
            array_l.append(b[0][0])
            array_r.append(b[1][0])
            b[0].remove(b[0][0])
            b[1].remove(b[1][0])
            
    if len(a[0]) > 0 :
        for item in a[0] :
            array_l.append(item)
        for item in a[1] :
            array_r.append(item)
            
    if len(b[0]) > 0 :
        for item in b[0] :
            array_l.append(item)
        for item in b[1] :
            array_r.append(item)
    
    return [array_l, array_r]

def binary_search(array, point, left, right) :
    if left > right :
        return -1
    m = int(np.floor(left + (right - left)/2))
    if point == array[m]:
        return m
    elif point > array[m] :
        return binary_search(array, point, m + 1, right)
    else :
        return binary_search(array, point, left, m - 1)
    
def binary_search_modified(array, point, left, right, index) :
    if left > right :
        return index
    m = int(np.floor(left + (right - left)/2))
    if point >= array[m] :
        index = m
        return binary_search_modified(array, point, m + 1, right, index)
    else :
        return binary_search_modified(array, point, left, m - 1, index)
 
def overlap_count_optimized(segments, points) :
    overlap = []
    segments_sorted = merge_sort_modified(segments, 0, len(segments[0]) - 1)
    for point in points :
        index = binary_search_modified(segments_sorted[0], point, 0, len(segments[0]) - 1, -1)
        count = 0
        if index != -1 :
            right_segments = segments_sorted[1][0:index + 1]
            right_segments_sorted = merge_sort(right_segments, 0, len(right_segments) - 1)
            index_2 = binary_search_modified(right_segments_sorted, point, 0, len(right_segments_sorted) - 1, -1)
            count = len(right_segments_sorted) - (index_2 + 1)
        overlap.append(count)
    return overlap

if __name__ == "__main__" :
    s, p = map(int, input().split())
    segments_l = []
    segments_r = []
    for i in range(0, s) :
        a, b = map(int, input().split())
        segments_l.append(a)
        segments_r.append(b)
    segments = [segments_l, segments_r]
    points = list(map(int, input().split()))
    print(*overlap_count_optimized(segments, points))