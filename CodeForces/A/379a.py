a,b = [int(i) for i in input().split()]
count = 0
res = 0
while a > 0:
    res+=1
    a-=1
    count+=1
    if count == b:
        a+=1
        count=0
print(str(res))
