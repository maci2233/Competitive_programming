q = int(input())
res = ''
for _ in range(q):
    n,k = [int(i) for i in input().split()]
    ki = 0
    for _ in range(n):
        res+=chr(ki%k + 97)
        ki+=1
    res+='\n'
print(res)
