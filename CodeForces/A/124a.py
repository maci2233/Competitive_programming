n,a,b = [int(i) for i in input().split()]
pos = n-a
beh = n-(a+1)
if beh > b:
    pos -= beh-b
print(str(pos))
