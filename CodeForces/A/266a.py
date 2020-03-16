num = int(input())
stones = input()
n = len(stones)
res = 0
for i in range(n-1):
    if stones[i] == stones[i+1]:
        res+=1
print(str(res))
