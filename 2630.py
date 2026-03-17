n = int(input())
ans = [0, 0]

arr = [list(map(int, input().split())) for _ in range(n)]
    
def checkfour( row: int, col: int, size: int) -> None :
    first = arr[row][col]

    for i in range(row, row+size):
        for j in range(col, col+size):
            if arr[i][j] != first:
                half = size // 2
                checkfour(row, col, half)
                checkfour(row + half, col, half)
                checkfour(row, col + half, half)
                checkfour(row + half, col + half, half)
                return

    ans[first] += 1

checkfour(0,0,n)

print(ans[0])
print(ans[1])