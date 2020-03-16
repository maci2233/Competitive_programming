def uniforms():
    n=int(input())
    loc = []
    vis = []
    for i in range(n):
        test = [int(i) for i in input().split()]
        loc.append(test[0])
        vis.append(test[1])
    res = 0
    for e in loc:
        for j in vis:
            if e == j:
                res+=1
    return res

print(str(uniforms()))
