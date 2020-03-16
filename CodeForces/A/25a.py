n = int(input())
nums = [int(i) for i in input().split()]
par = []
impar = []
for i in range(n):
    if nums[i] % 2 == 0:
        par.append(i+1)
    else:
        impar.append(i+1)
    if len(par) >= 2 and len(impar) == 1:
        print(impar[0])
        break
    elif len(impar) >= 2 and len(par) == 1:
        print(par[0])
        break
