test = int(input())
res = 0
for i in range(test):
    dorm = input().split()
    if int(dorm[1]) - int(dorm[0]) >= 2:
        res+=1
print(res)
