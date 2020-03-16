def check_seats(i,j):
    if i == 'O' and j == 'O':
        return True
    return False

n = int(input())
solved = False
rows = []
for _ in range(n):
    row = input()
    if solved:
        print(row)
        continue
    if check_seats(row[0], row[1]):
        solved = True
        print("YES")
        for e in rows:
            print(e)
        print('++' + row[2:5])
        continue
    if check_seats(row[3], row[4]):
        solved = True
        print("YES")
        for e in rows:
            print(e)
        print(row[0:3] + '++')
        continue
    rows.append(row)
if not solved:
    print("NO")
