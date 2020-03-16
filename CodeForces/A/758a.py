def macinco():
    n=int(input())
    if n == 1:
        return 0
    nums = [int(i) for i in input().split()]
    nums.sort(reverse=True)
    max = nums[0]
    res = 0
    for i in range(1,n):
        res+=max-nums[i]
    return res

print(str(macinco()))
