def max_sum(n,m):
    return summatory(n-m)

def min_sum(n,m):
    di,mo = divmod(n,m)
    if mo == 0:
        return summatory(di-1)*m
    else:
        return summatory(di)*mo

def summatory(num):
    return int((num**2/2)+(num/2))

def main():
    n,m = [int(i) for i in input().split()]
    res = str(min_sum(n,m)) + ' ' + str(max_sum(n,m))
    print(res)

main()
