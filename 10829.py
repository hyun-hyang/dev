n = int(input())

def jinsu (n : int = 1) -> int:
    if n == 0:
        return 0
    return n % 2 + jinsu((n //2)) * 10
print(jinsu(n))