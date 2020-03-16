s = input()
n = len(s)
rep = [0]*n
for i in range(1,n):
    if s[i-1] == s[i]:
        rep[i] = rep[i-1] + 1
    else:
        rep[i] = rep[i-1]
res = ''
q = int(input())
for _ in range(q):
    low,high = [int(i) for i in input().split()]
    res+=str(rep[high-1] - rep[low-1]) + '\n'
print(res)
