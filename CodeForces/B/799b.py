n = int(input())
ps = [int(i) for i in input().split()]
front = [int(i) for i in input().split()]
back = [int(i) for i in input().split()]
colors = [[], [], []]
lens = [0] * 3
inds = [0] * 3
for p, f, b, i in zip(ps, front, back, [i for i in range(n)]):
    colors[f-1].append((p, i))
    lens[f-1] += 1
    if b != f:
        colors[b-1].append((p, i))
        lens[b-1] += 1
for i in range(3):
    colors[i].sort()
m = int(input())
favs = [int(i) for i in input().split()]
bought = set()
res = ''
for fav in favs:
    while True:
        if inds[fav-1] == lens[fav-1]:
            res += '-1 '
            break
        if colors[fav-1][inds[fav-1]][1] in bought:
            inds[fav-1] += 1
        else:
            res += str(colors[fav-1][inds[fav-1]][0]) + ' '
            bought.add(colors[fav-1][inds[fav-1]][1])
            break
print(res[:-1])
