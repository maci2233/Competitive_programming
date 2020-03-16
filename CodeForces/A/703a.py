n = int(input())
m = 0
c = 0
for _ in range(n):
    l,r = [int(i) for i in input().split()]
    if l > r:
        m+=1
    elif l < r:
        c+=1
    else:
        continue
if m > c:
    print("Mishka")
elif m == c:
    print("Friendship is magic!^^")
else:
    print("Chris")
