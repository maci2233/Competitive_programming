num,n = [int(i) for i in input().split()]
for _ in range(n):
    if num % 10 == 0:
        num//=10
    else:
        num-=1
print(str(num))
