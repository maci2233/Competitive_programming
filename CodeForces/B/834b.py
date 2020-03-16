n, k = map(int, input().split())
doors = input()
close_i = {}
opened = set()
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    close_i[c] = doors.rfind(c)
guards = 0
for i, d in enumerate(doors):
    if i == close_i[d]:
        if d in opened:
            opened.remove(d)
            guards -= 1
        elif guards+1 > k:
            print("YES")
            break
        continue
    if d not in opened:
        opened.add(d)
        guards += 1
        if guards > k:
            print("YES")
            break
else:
    print("NO")
