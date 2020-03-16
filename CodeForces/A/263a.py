matrix = []
n = 5
for i in range(n):
    row = input().split()
    matrix.append(row)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            print(abs((i-2)) + abs((j-2)))
            break
