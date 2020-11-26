import os
import numpy as np


def overlap_v0(points, n):
    points = np.array(points)
    points = points[np.lexsort((points[:,1], points[:,0]))]
    overlap = []
    current_index = 0
    overlap_point = 0    
    while current_index < n :
        float_index = current_index
        overlap_point = points[current_index][1]
        
        while float_index < n -1 and points[float_index + 1][1] <= points[float_index][1] and  points[float_index + 1][0] <= points[float_index][1]:
            overlap_point = points[float_index + 1][1]
            float_index += 1
        
        while current_index < n - 1 and overlap_point >= points[current_index + 1][0] and overlap_point <= points[current_index + 1][1] :
            current_index += 1
            
        current_index += 1
        overlap.append(overlap_point)
    return overlap

def overlap_v1(points, n) :
    points = np.array(points)
    points = points[np.lexsort((points[:,1], points[:,0]))]
    overlap = []
    current_index = 0
    overlap_point = 0
   
    while current_index < n :
        common_left = points[current_index][0]
        common_right = points[current_index][1]
        
        while current_index < n - 1 and points[current_index + 1][0] <= common_right:
            common_left = max(common_left, points[current_index + 1][0])
            common_right = min(common_right, points[current_index + 1][1])
            current_index += 1

        overlap.append(common_left)
        current_index += 1
    return overlap


if __name__ == "__main__" :
    n = int(input())
    points = []
    for i in range(0, n) :
        a, b = map(int, input().split())
        points.append([a,b])
    overlap_arr = overlap_v1(points, n)
    print(len(overlap_arr))
    print(*overlap_arr, sep = ' ')
    #print(overlap_arr)