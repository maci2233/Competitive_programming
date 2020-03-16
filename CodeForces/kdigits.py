n = 10
k = 0
count = 0
for i in range(n+1):
    num = i
    while True:
        if num % 10 == k:
            count+=1
        num=num//10
        if num == 0:
            break
print(str(count))
