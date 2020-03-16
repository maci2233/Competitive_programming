n = int(input())
sumx=0
sumy=0
sumz=0
for i in range(n):
    coords = input().split()
    sumx += int(coords[0])
    sumy += int(coords[1])
    sumz += int(coords[2])
if sumx == 0 and sumy == 0 and sumz == 0:
    print("YES")
else:
    print("NO")
