#Cada iteracion checas si el row y col ya fueron eliminados
#si row no esta le restas el largo del tablero menos el numero de cols que ya mataste
# si col no esta le restas el largo del tablero menos el numero de rows que ya mataste
n, m = map(int, input().split())
total = n*n
death = 0
res = ''
rows, cols = set(), set()
n_rows, n_cols = 0, 0
for _ in range(m):
    row, col = map(int, input().split())
    if row not in rows:
        rows.add(row)
        n_rows += 1
        death += n - n_cols
    if col not in cols:
        cols.add(col)
        n_cols += 1
        death += n - n_rows
    res += str(total - death) + ' '
print(res[:-1])
