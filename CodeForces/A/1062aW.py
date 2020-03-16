def sale():
    n = int(input())
    nums = [int(i) for i in input().split()]
    res = 0
    res_men = 0
    res_mas = 0
    if n == 2:
        if nums[0] == 999 or nums[1] == 2:
            return 1
        else:
            return 0
    for i in range(0, n):
        if nums[i]-1 == i:
            res_men = i
        elif nums[n-1] == 1000 and 1000 - nums[i] == n-1 - i and n-1 - i > res_mas:
            res_mas = n-1-i
        elif n-1 != i and i != 0:
            if nums[i-1] == nums[i]-1 and nums[i]+1 == nums[i+1] and res_mas == 0:
                res_men+=1
    return res_men + res_mas


def main():
    print(str(sale()))


main()
