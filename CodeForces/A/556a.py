def oz():
    n = int(input())
    if n == 1:
        return 1
    nums = [int(i) for i in input()]
    nums.sort()
    res = 0
    i=0
    j=n-1
    while nums[i] == 0 and nums[j] == 1:
        n-=2
        i+=1
        j-=1
    return n

print(str(oz()))
