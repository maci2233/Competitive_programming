ind = [-1] * 4
need = 1
arr = input()
n = len(arr)
for i in range(n):
    if need == 1:
        if arr[i] == '[':
            ind[0] = i
            need += 1
    elif need == 2:
        if arr[i] == ':':
            ind[1] = i
            break
need = 4
for i in range(n-1, -1, -1):
    if need == 4:
        if arr[i] == ']':
            ind[3] = i
            need -= 1
    elif need == 3:
        if arr[i] == ':':
            ind[2] = i
            break
if ind[1] == ind[2] or ind != sorted(ind):
    print(-1)
    exit()
for i in range(4):
    if ind[i] == -1:
        print(-1)
        exit()
res = 4 + (ind[2] - 1 - ind[1])
for i in range(ind[1]+1, ind[2]):
    if arr[i] != '|':
        res -= 1
print(res)
