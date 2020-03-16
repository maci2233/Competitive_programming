test = input().split()
cost = int(test[0])
money = int(test[1])
n = int(test[2])
total = 0
for i in range(n):
    total = total + cost*(i+1)
res = total - money
if res < 0:
    print("0")
else:
    print(str(res))
