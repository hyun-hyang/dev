n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = [0, 0, 0]

def sol(row: int, col:int, size:int):
    first = arr[row][col]

    if size == 1:
        result[first + 1] += 1
        return

    for x in range( row, row+size):
        for y in range( col, col+size):
            if arr[x][y] != first:
                next_size = size // 3

                for nr in row, row + next_size, row + next_size * 2:
                    for nc in col, col + next_size, col + next_size * 2:
                        sol(nr, nc, next_size)
                return
            
    result[first + 1] += 1
    
sol(0, 0, n)

for i in result:
    print(i)