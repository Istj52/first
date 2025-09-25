def fibonacci_numbers (x): 
    if x == 0: return 0
    elif x == 1 or x == 2: 
        return 1
    else:
        return (fibonacci_numbers(x-1)+fibonacci_numbers(x-2))