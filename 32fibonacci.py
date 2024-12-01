# 32fibonacci.py by mohammed

def fibonacci(n):
"""
This function will print the numbers
of the Fibonacci sequence "n" times
"""
    a = 0               # the sequence will start of with 0 and 1
    b = 1
    for i in range(n):  
        print(a)       # initial 0
        hold = b       # this will hold the value of b 
        b = a + b      # this will update the value of b to the next number
        a = hold       # this will update the value of a to the next number
        
print(fibonacci(10))

