n,m = [int(i) for i in input().split()]
tasks = [1] + [int(i) for i in input().split()]
res = 0
i = 0
while i < m:
    if tasks[i] < tasks[i+1]:
        res+=tasks[i+1] - tasks[i]
    elif tasks[i] > tasks[i+1]:
        res+=n - tasks[i] + tasks[i+1]
    else:
        while tasks[i] == tasks[i+1]:
            i+=1
            if i == m:
                break
        continue
    i+=1
print(str(res))
