x = int(input())
n = x//2
print(str(n))
res = ""
for _ in range(n-1):
    res+="2 "
if x % 2 == 0:
    res+="2"
else:
    res+="3"
print(res)
