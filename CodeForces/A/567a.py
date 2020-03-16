n = int(input())
cits = [int(i) for i in input().split()]
res = ''
res+=str(cits[1]-cits[0]) + ' ' + str(cits[n-1]-cits[0]) + '\n'
for i in range(1, n-1):
    res+=str(min(cits[i]-cits[i-1], cits[i+1]-cits[i])) + ' ' + str(max(cits[i]-cits[0],cits[n-1]-cits[i])) + '\n'
res+=str(cits[n-1]-cits[n-2]) + ' ' + str(cits[n-1]-cits[0])
print(res)
