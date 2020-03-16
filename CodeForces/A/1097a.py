c = input()
cards = [i for i in input().split()]
for card in cards:
    if c[0] == card[0] or c[1] == card[1]:
        print('YES')
        exit()
print('NO')
