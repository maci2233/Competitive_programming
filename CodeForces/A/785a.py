n = int(input())
res = 0
figs = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
for _ in range(n):
    res+=figs[input()]
print(str(res))
