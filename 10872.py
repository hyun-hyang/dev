n = int(input())

def factorial(n: int) -> int:
    if n == 0:
        return 1    
    else:
        return factorial (n-1) * n

print(factorial(n))