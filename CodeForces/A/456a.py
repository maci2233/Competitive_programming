def laptops():
    n = int(input())
    laptop = []
    for _ in range(n):
        c,q = [int(i) for i in input().split()]
        laptop.append((c,q))
    laptop.sort()
    for i in range(n-1):
        if laptop[i][1] > laptop[i+1][1]:
            return "Happy Alex"
    return "Poor Alex"

print(laptops())
