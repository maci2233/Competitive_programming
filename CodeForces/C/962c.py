#este es a mega fuerza bruta, tengo un arreglo con todos los numeros desde el 1
#hasta la raiz de 2*10**9 y para cada uno empezando del mayor checo si tiene
#una common subsequence en el input, si si hay uno entonces resto el largo del
#input - el largo del numero actual
from math import ceil, sqrt

num = input()
n = len(num)
lim = ceil(sqrt(2 * 10**9))
nums = [str(int(i**2)) for i in range(lim, 0, -1)]
for sq in nums:
    if len(sq) > n:
        continue
    ind = 0
    for dig in sq:
        ind = num.find(dig, ind, n)
        if ind == -1:
            break
        else:
            ind += 1
    else:
        print(n - len(sq))
        break
else:
    print(-1)
