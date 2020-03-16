n = int(input())
input = [int(i) for i in input().split()]
aux = [0] * n
res = ""
for i in range(n):
    aux[input[i] - 1] = i+1
for i in aux:
    res+=str(i) + " "
print(res)
