test = input().split()
n = int(test[0])
test = [int(i) for i in test[1::]]
test.sort()
a = test[0]
b = test[1]
c = test[2]
mat = [[a] + [-1]*n, [b] + [-1]*n, [c] + [-1]*n]
for i in range(1,n+1):
    if i % a == 0:
        mat[0][i] = i//a
for i in range(1,3):
    num = mat[i][0]
    for j in range(1,n+1):
        if mat[i-1][j] != -1:
            mat[i][j] = mat[i-1][j]
        if num > j:
            continue
        ind = j-num
        if ind == 0:
            if mat[i][j] == -1:
                mat[i][j] = 1
        elif mat[i][ind] != -1:
            aux = mat[i][ind]+1
            if aux > mat[i][j]:
                mat[i][j] = aux
print(mat[2][n])
