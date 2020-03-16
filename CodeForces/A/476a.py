def number():
    test = input().split()
    n = int(test[0])
    m = int(test[1])
    if n < m:
        return -1
    steps = 0
    sum = 0
    while n-sum > m:
        steps=steps+1
        sum=sum+2
    steps=steps+(n-sum)
    if steps % m == 0:
        return steps
    floor = (steps//m)*m
    if floor*2 >= n:
        return floor
    else:
        return ((steps//m)+1)*m

print(str(number()))
