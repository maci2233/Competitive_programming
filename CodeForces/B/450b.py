nums = [int(i) for i in input().split()]
n = int(input())
for i in range(1,5):
    nums.append(nums[i] - nums[i-1])
n = (n-1) % 6
print(nums[n] % 1000000007)
