#Para cada jarra hay 2 casos
# - comes de la jarra 3 veces k cantidad
# - comes de la jarra menos de 3 veces hasta que se acabe o hasta que lo que sobra sea menor a k
w, r = open('output.txt', 'w'), open('input.txt', 'r')
n, k = map(int, r.readline().split())
t = list(map(int, r.readline().split()))
w.write(str(sum(max(i % k, i - 3 * k) for i in t)))
