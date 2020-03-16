n = int(input())
studs = [int(i) for i in input().split()]
sums = sum(studs)
maxs = max(studs)
votes = 0
while votes < sums:
    votes = (maxs*n) - sums
    if votes > sums:
        print(str(maxs))
    else:
        maxs+=1
        votes = 0
