import os
import numpy as np


def compare_numbers(num1, num2) :
    combo1 = num1 + num2
    combo2 = num2 + num1
    
    if combo1 >= combo2 :
        return num1
    else :
        return num2

def largest_number(numbers) :
    largest_numb = []
    
    while len(numbers) > 0 :
        largest_val = numbers[0]
        for vals in numbers :
            largest_val = compare_numbers(largest_val, vals)
        largest_numb.append(largest_val)
        numbers.remove(largest_val)
    
    return int("".join(largest_numb))


if __name__ == "__main__" :
    n = int(input())
    numbers = input().split()
    print(largest_number(numbers))