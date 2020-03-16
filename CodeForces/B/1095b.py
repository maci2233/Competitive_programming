def ins():
    n = int(input())
    if n == 2:
        return 0
    nums = [int(i) for i in input().split()]
    ma = max(nums)
    mi = min(nums)
    pos_res = ma-mi
    nums.remove(ma)
    pos_res = min(pos_res, max(nums) - mi)
    nums.append(ma)
    nums.remove(mi)
    pos_res = min(pos_res, ma - min(nums))
    return pos_res

print(ins())
