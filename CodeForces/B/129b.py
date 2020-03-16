import copy

n, m = [int(i) for i in input().split()]
ties = {i:[] for i in range(1, n+1)}

for _ in range(m):
    s1, s2 = map(int, input().split())
    ties[s1].append(s2)
    ties[s2].append(s1)

res = 0
while True:
    expelled = False
    tmp_ties = copy.deepcopy(ties)
    for k, v in ties.items():
        if len(v) == 1:
            expelled = True
            if v[0] in tmp_ties:
                tmp_ties[v[0]].remove(k)
            del tmp_ties[k]
    if expelled:
        res += 1
        ties = copy.deepcopy(tmp_ties)
    else:
        break

print(res)
