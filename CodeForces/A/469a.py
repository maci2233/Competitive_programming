n = int(input())
new = input().split()[1:] + input().split()[1:]
levels = set(new)
if len(levels) >= n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
