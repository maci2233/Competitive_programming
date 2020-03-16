n = int(input())
nums = [int(i) for i in input().split()]
start = -1
end = -1
inv = False
for i in range(1,n):
    if nums[i] < nums[i-1]:
        if start == -1:
            start = i
            inv = True
        end = i+1
    elif not inv:
        continue
    else:
        break
if start == -1 and end == -1:
    print('yes\n1 1')
else:
    nums = nums[:start-1] + nums[start-1:end][::-1] + nums[end:]
    if nums == sorted(nums):
        print('yes\n'+str(start) + ' ' + str(end))
    else:
        print('no')
