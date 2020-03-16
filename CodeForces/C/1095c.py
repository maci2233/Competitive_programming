from bisect import bisect_right
def main():
    res = []
    n,k = [int(i) for i in input().split()]
    if n < k:
        return []
    mult = 1
    mults = []
    while mult < 1000000001:
        mults.append(mult)
        mult *= 2
    while n > 0 and k > 0:
        i = bisect_right(mults,n) - 1
        tmp_n = n - mults[i]
        k -= 1
        if tmp_n > 0 and k == 0:
            return []
        while tmp_n < k and i >= 0:
            i -= 1
            tmp_n = n - mults[i]
        n = tmp_n
        res.append(mults[i])
    return res

res = main()
if len(res) == 0:
    print('NO')
else:
    print('YES')
    print(*res)
