import numpy as np
import os

def create_number(number, length) :
    new_number = number.ljust(length, '0')
    return new_number

def compare_number(num1, num2) :
    

def largest(numbers) :
    numbers = list(numbers)
    raw_sequence = "".join(numbers)
    max_length = len(raw_sequence)
    max_sequence = []
    remove = -1
    max_number_def = '0'
    while len(numbers) > 0 :
        length = max_length - len("".join(max_sequence)) 
        max_number = create_number(max_number_def, length)    
        for number in numbers :
            new_number = create_number(number, length)
            if new_number > max_number :
                max_number = new_number
                remove = number
        max_sequence.append(remove)
        numbers.remove(remove)
    
    return "".join(max_sequence)         
            
            
if __name__ == "__main__" :
    n = int(input())
    numbers = map(int, input().split())
    numbers = [str(x) for x in numbers]
    print(largest(numbers))