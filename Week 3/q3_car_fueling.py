import os 
import numpy as np

def refills(m, stations, n) :
    n_refills = 0
    current_index = 0
    refills= []
    
    while current_index <= n :
        last_refill = current_index
        refills.append(stations[last_refill])
        while current_index <= n and stations[current_index + 1] - stations[last_refill] <=m :
            current_index += 1
            
        if current_index == last_refill :
            return -1
    
    return len(refills) - 1
    

if __name__ == "__main__" :
    d = int(input())
    m = int(input())
    n = int(input())
    station_list = map(int, input().split())
    stations = []
    stations.append(0)
    for station in station_list :
        stations.append(station)    
    stations.append(d)    
    print(refills(m, stations, n))