n,m = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
seen = set()
memo = [1]*n
res = ''
seen.add(nums[n-1])
for i in range(n-2,-1,-1):
    if nums[i] not in seen:
        seen.add(nums[i])
        memo[i] = memo[i+1]+1
    else:
        memo[i] = memo[i+1]
for _ in range(m):
    f = int(input())
    res+=str(memo[f-1]) + '\n'
print(res)
