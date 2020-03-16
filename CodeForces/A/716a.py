n,t = [int(i) for i in input().split()]
words = [int(i) for i in input().split()]
res = 1
for i in range(1,n):
    if words[i] - words[i-1] <= t:
        res+=1
    else:
        res = 1
print(str(res))
