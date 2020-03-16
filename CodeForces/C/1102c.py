from bisect import bisect_right
n,x,y = [int(i) for i in input().split()]
if x > y:
    print(n)
    exit()
nums = sorted([int(i) for i in input().split()])
ind = bisect_right(nums, x) - 1
c = 0
while ind != -1:
    del nums[ind]
    n -= 1
    c += 1
    if n == 0:
        break
    nums[0] += y
    nums.sort()
    ind = bisect_right(nums, x) - 1
print(c)
