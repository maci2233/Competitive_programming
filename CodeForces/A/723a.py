dists = [int(i) for i in input().split()]
dists.sort()
res = dists[1] - dists[0] + dists[2] - dists[1]
print(str(res))
