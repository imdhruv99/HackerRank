import sys

def Fibonacci(n):
    fn_2 = 1 
    fn_1 = 1
    sum = 0
    while True :
        fn = fn_2 + fn_1 
        if fn >= n: 
            return sum
        if fn % 2 == 0: 
            sum += fn
        fn_2, fn_1 = fn_1, fn
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(Fibonacci(n))