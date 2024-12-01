# 31fizzbuzz.py by mohammed

limit = 101                     # 101 so it actually gets to 100
"""
This program will loop 1's until we get
to a 100. For each number divisible by 3
we get Fizz, if its by 5 we get Buzz. If
the number is divisible by both, we get
FizzBuzz!
"""
for i in range(1, limit):
    if i % 3 == 0 and i % 5 == 0: 
        print(i , 'FizzBuzz')
    elif i % 3 == 0:   
        print(i , 'Fizz')
    elif i % 5 == 0:
        print(i , 'Buzz')
    else:
        print(i)
