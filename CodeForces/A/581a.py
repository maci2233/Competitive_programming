a,b = [int(i) for i in input().split()]
res = 0
while a > 0 and b > 0:
    res+=1
    a-=1
    b-=1
extra=(a+b)//2
print(str(res)+" "+str(extra))
