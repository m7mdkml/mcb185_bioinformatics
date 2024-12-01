# 35nchoosek.py by mohammed

def factorial(x):      
"""
once defined you are able to use its out put so seamlessly!
"""
    if x == 0: return 1
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result
"""
reusing the factorial function, its then "plugged in" 
the nchoosek function to solve a different formula
"""
def nchoosek(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
    
print(nchoosek(5, 2)) 
print(nchoosek(0, 0))
print(nchoosek(10, 4))

def euler(value):     
    e_sum = 0
    for f in range(value):
        e_sum = e_sum + 1 / factorial(f)
    return e_sum
    

