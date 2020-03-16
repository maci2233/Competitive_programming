#En este problema solo me importa el numero mas bajo de las ps porque la unica forma
# en que F(x) = x es si... a % ps, a < ps. Obtengo el valor minimo de las Pi
# y luego obtengo la diferencia entre ese pi - a y le resto la diferencia entre
# pi-b+1 y ya con eso tengo solamente los F(x) = x dentro del rango [a-b]
nums = [int(i) for i in input().split()]
ps = min(nums[:-2])
a, b = nums[-2], nums[-1]
res = max(0, ps-a)
print(res - max(0, ps-(b+1)))
