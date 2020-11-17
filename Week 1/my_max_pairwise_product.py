import os
import random
#os.chdir('E:\Coursera\Algo Toolbox\Assignment')

def max_pairwise_brute(n, numbers):
    max_product = 0
    for i in range(0, n) :
        for j in range(i + 1, n) :
            product = numbers[i] * numbers[j]
            if product > max_product :
                max_product = product
    
    return max_product

def max_pairwise_better(n, numbers) :
    max_index1 = -1
    max_index2 = -1
    max_number1 = -1
    max_number2 = -1
    for i in range(0, n) :
        if numbers[i] > max_number1 :
            max_index1 = i
            max_number1 = numbers[i]
    
    for j in range(0, n) :
        if numbers[j] > max_number2 and j != max_index1 :
            max_index2 = j
            max_number2 = numbers[j]
            
    return numbers[max_index1] * numbers[max_index2]    

seed = 2156

def stress_test(seed, max_n, min_size, max_size) :
    random.seed(seed)
    while True :
        n_items = random.randint(2, max_n)
        items = random.sample(range(min_size, max_size), n_items)
        product1 = max_pairwise_brute(n_items, items)
        product2 = max_pairwise_better(n_items, items)
        print(n_items, '\n')
        print(items, "\n")
        if product1 != product2 :
            print("Error", product1, product2)
        else:
            print("Okay!")
        print("\n")
    return 
    
    
if __name__ == "__main__" :
    input_len = int(input())
    numbers = [int(x) for x in input().split()]
    stress_test(seed, 100, 1, 10000)
    product = max_pairwise_better(input_len, numbers)
    print(product)