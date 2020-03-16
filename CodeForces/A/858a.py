#TIME LIMIT EXCEEDED
n,k = [int(i) for i in input().split()]
exp=10**k
while True:
    if exp % n == 0:
        count = 0
        for e in str(exp):
            if e == '0':
                count+=1
        if count >= k:
            print(str(exp))
            break
    exp+=1
