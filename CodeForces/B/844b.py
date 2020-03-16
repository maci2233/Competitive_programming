n, m = map(int, input().split())
mat = []
for i in range(n):
    mat.append([int(i) for i in input().split()])
cont = n*m
for row in mat:
    ones = row.count(1)
    cont += 2**ones - (ones+1)
    zeroes = row.count(0)
    cont += 2**zeroes - (zeroes+1)
mat = map(list, zip(*mat))
for row in mat:
    ones = row.count(1)
    cont += 2**ones - (ones+1)
    zeroes = row.count(0)
    cont += 2**zeroes - (zeroes+1)
print(cont)
