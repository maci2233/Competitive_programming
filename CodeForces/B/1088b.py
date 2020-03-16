n,k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
nums.sort()
aux = 0
i = 0
for _ in range(k):
    if i >= n or nums[n-1]-aux == 0:
        print('0')
        continue
    while nums[i]-aux <= 0 and i < n:
        i+=1
    print(str(nums[i] - aux))
    aux+=nums[i]-aux
