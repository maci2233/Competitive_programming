cents = 80
coins = [1, 10, 25]
mat = [[0 for j in range(cents+1)] for i in range(len(coins))]
for i in range(len(mat[0])):
    mat[0][i] = i // coins[0]
for i in range(1, len(mat)):
    for j in range(len(mat[i])):
        if coins[i] > j:
            mat[i][j] = mat[i-1][j]
        else:
            dif = j - coins[i]
            mat[i][j] = min(mat[i-1][j], 1 + mat[i][dif])


print(mat[-1][-1])
