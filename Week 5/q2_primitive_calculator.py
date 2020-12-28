import numpy as np

def calculator_v0(n) :
    print("n :", n)
    print("number :", number)    
    if n  not in number :
        number[n] = n
        while n > 1 :
            num_1, num_2, num_3 = -1,-1,-1
            if n % 2 == 0 :
                num_2 = calculator_v0(int(n/2)) + 1
            if n % 3 == 0 :
                num_3 = calculator_v0(int(n/3)) + 1
            if n - 1 >= 0 :
                num_1 = calculator_v0(n-1) + 1
            num = [num_1, num_2, num_3]
            num_2 = [n - 1, int(n/2), int(n/3)]
            num_copy = num[:]
            num_2_copy = num_2[:]
            if len(num) > 0 :
                for i in range(len(num)) :
                    if num[i] == -1:
                        num_copy.remove(num[i])
                        num_2_copy.remove(num_2[i])
            print(num_copy, num_2_copy)
            number[n] = min(num_copy)
            n = num_2_copy[num_copy.index(min(num_copy))]
        
    return number[n] 

def calculator_v1(n) :
    numbers = np.zeros(n + 1, dtype = int) 
    array = []
    for i in range(1, n + 1) :
        num_1, num_2, num_3 = -1, -1, -1
        if i - 1 > 0 :
            index_1 = i - 1
            num_1 = numbers[index_1] + 1
        if i % 2 == 0 :
            index_2 = int(i/2)
            num_2 = numbers[index_2] + 1
        if i % 3 == 0:
            index_3 = int(i/3)
            num_3 = numbers[index_3] + 1
        num = [num_1, num_2, num_3]
        num = [x for x in num if x != -1]
        if len(num) > 0 :
            numbers[i] = min(num)
    index = n
    array.append(n)
    while index > 1 :
        temp_num = []
        temp_index = []
        if index - 1 > 0 :
            temp_num.append(numbers[index - 1])
            temp_index.append(index - 1)
        if index % 2 == 0 :
            temp_num.append(numbers[int(index/2)])
            temp_index.append(int(index/2))
        if index % 3 == 0:
            temp_num.append(numbers[int(index/3)])
            temp_index.append(int(index/3))
        if len(temp_num) == 0 :
            break
        index = temp_index[temp_num.index(min(temp_num))]
        array.append(index)
    return numbers[n], array

def calculator_v2(n) :    
     if n not in number :
        num_1, num_2, num_3 = -1,-1,-1
        if n % 2 == 0 :
            num_2 = calculator_v2(int(n/2)) + 1
        if n % 3 == 0 :
            num_3 = calculator_v2(int(n/3)) + 1
        if n - 1 > 0 :
            num_1 = calculator_v2(n-1) + 1
        num = [num_1, num_2, num_3]
        num_2 = [n - 1, int(n/2), int(n/3)]
        num_copy = num[:]
        num_2_copy = num_2[:]
        if len(num) > 0 :
            for i in range(len(num)) :
                if num[i] == -1:
                    num_copy.remove(num[i])
                    num_2_copy.remove(num_2[i])
        number[n] = min(num_copy)
     return number[n]

if __name__ == "__main__" :
    n = int(input())
    number = dict()
    number[1] = 0
    count, array = calculator_v1(n)
    print(count)
    print(*array[::-1])