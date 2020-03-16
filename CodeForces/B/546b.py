n = int(input())
badges = [int(i) for i in input().split()]
badges.sort()
cnt = [0] * 7000
m = len(cnt)
c = 0
for e in badges:
    cnt[e] += 1
for i in range(m):
    j = i
    aux = 0
    while cnt[i] > 1:
        while cnt[j] > 0:
            aux += 1
            j += 1
            if j == m:
                break
        c += aux
        cnt[j] = 1
        cnt[i] -= 1
print(c)
