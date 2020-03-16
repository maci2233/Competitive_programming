test = input().split()
n = int(test[0])
m = int(test[1])
puzzles = [int(i) for i in input().split()]
puzzles.sort()
min = puzzles[n-1] - puzzles[0]
x = len(puzzles) - (n-1)
for i in range(x):
    aux = puzzles[i+n-1] - puzzles[i]
    if aux < min:
        min = aux
print(str(min))
