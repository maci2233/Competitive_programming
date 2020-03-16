numbers = input().split('+')
numbers.sort()
res = "" + numbers[0]
n = len(numbers)
for i in range(1, n):
    res = res + "+" + numbers[i]
print(res)
