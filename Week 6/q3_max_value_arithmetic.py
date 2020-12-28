import numpy as np

def max_value(digits, operators) :
    for i in range(n_digits) :
        min_array[i][i] = digits[i]
        max_array[i][i] = digits[i]
    
    for i in range(n_digits - 1) :
        
    

if __name__ == "__main__" :
    string = input()
    digits = []
    operators = []
    for i in range(len(string)) :
        if i % 2 == 0 :
            digits.append(int(string[i]))
        else:
            operators.append(string[i])
    n_digits = len(digits)
    min_array = np.zeros((n_digits, n_digits), dtype = int)
    max_array = np.zeros((n_digits, n_digits), dtype = int)
    print(max_value(digits, operators))