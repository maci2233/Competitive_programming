n = int(input())
lock1 = input()
lock2 = input()
res = 0
for i in range(n):
    n1 = int(lock1[i])
    n2 = int(lock2[i])
    if n1 == n2:
        continue
    elif n1 > n2:
        a = 9-n1+1+n2
        b = n1-n2
    else:
        a = n2-n1
        b = n1+1+9-n2
    res+=min(a,b)
print(str(res))
