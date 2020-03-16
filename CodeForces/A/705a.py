n = int(input())
flag = 1
res = ""
for i in range(n):
    if flag == 1:
        res+="I hate "
    else:
        res+="I love "
    if i+1 < n:
        res+="that "
    flag*=-1
res+="it"
print(res)
