import sys


def recursion(s:str, l:int, r:int, cnt:int) -> tuple[int, int]:
    if l >= r:
        return 1, cnt
    elif s[l] == s[r]:
        return recursion(s, l+1, r-1, cnt+1)
    else:
        return 0, cnt

def isPalindrome(s:str) -> tuple[int, int]:
    return recursion(s, 0, len(s)-1, 1)

testcase_cnt = int(sys.stdin.readline().rstrip('\n'))

for _ in range(testcase_cnt):
    S = sys.stdin.readline().rstrip('\n')
    a: tuple[int,int] = isPalindrome(S)
    print(a[0], a[1])