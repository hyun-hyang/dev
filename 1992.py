n = int(input())
arr = [list(map(int, str(input()))) for _ in range (n)]

def sol(size: int) -> None:
    next_size = size //2
    next_arr = [[" "]* next_size for _ in range (next_size)]

    next_arr

    for x in range(next_size):
        for y in range(next_size):
            if arr[x][x] == arr[x+1][x] == arr[x][y] == arr[x][y+1]:
                next_arr
