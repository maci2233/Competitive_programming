n,k = [int(i) for i in input().split()]
limit = 240-k
time = 5
res = 0
while limit >= time and n>0:
    limit-=time
    time+=5
    res+=1
    n-=1
print(str(res))
