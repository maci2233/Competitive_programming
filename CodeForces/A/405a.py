n = int(input())
cubes = [int(i) for i in input().split()]
cubes.sort()
res = ""
for i in cubes:
    res+=str(i) + " "
print(res)
