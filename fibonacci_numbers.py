def fibonacci_numbers (x): 
    if x == 0: return 0
    elif x == 1 or x == 2: 
        return 1
    else:
        return (fibonacci_numbers(x-1)+fibonacci_numbers(x-2))
a = int (input ("Enter the first number: "))
b = int (input ("Enter the second number: "))
print (fibonacci_numbers(a)+fibonacci_numbers(b))
