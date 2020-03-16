n = int(input())
numbers = [int(i) for i in input().split()]
res = 1
total = 1
for i in range(n-1):
    if numbers[i+1] >= numbers[i]:
        res+=1
        if total < res:
            total = res
    else:
        res = 1
print(str(total))
