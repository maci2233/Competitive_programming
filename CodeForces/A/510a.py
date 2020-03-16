n,m = [int(i) for i in input().split()]
res = ""
side = 1
for i in range(0,n):
    mod = False
    for j in range(m):
        if i % 2 != 0:
            mod = True
            if j == 0 and side == -1:
                res+="#"
            elif j+1 == m and side == 1:
                res+="#"
            else:
                res+="."
        else:
            res+="#"
    if mod:
        side*=-1
    print(res)
    res = ""
