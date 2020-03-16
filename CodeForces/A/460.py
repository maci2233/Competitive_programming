n,m = [int(i) for i in input().split()]
dias = 0
count = 0
while n > 0:
    n-=1
    count+=1
    dias +=1
    if count == m:
        n+=1
        count = 0
print(str(dias))
