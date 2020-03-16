tests = int(input())
res = 0
max = 0
for i in range(tests):
    test = input().split()
    res = res - int(test[0])
    res = res + int(test[1])
    if res > max:
        max = res
print(str(max))
