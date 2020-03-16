two,three,five,six = [int(i) for i in input().split()]
res = 0
low = min(two,five,six)
res+=256*low
two-=low
five-=low
six-=low
low = min(two,three)
res+=32*low
print(str(res))
