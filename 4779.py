cantoa = ["-"]

for i in range(1,13):
    tmp = cantoa[i-1] + " " * len(cantoa[i-1]) + cantoa[i-1]
    cantoa.append(tmp)

while True:
    try:
        n = int(input())
        print(cantoa[n])
    except EOFError:
        break