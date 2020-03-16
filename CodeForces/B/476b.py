s1 = input()
s2 = input()
ans = 0
pos = [0]
for e in s1:
    if e == '+':
        ans+=1
    else:
        ans-=1
for e in s2:
    m = len(pos)
    if e == '+':
        for i in range(m):
            pos[i]+=1
    elif e == '-':
        for i in range(m):
            pos[i]-=1
    else:
        for i in range(m):
            pos.append(pos[i]+1)
            pos[i]-=1
n = len(pos)
res = pos.count(ans)
print(res/n)
