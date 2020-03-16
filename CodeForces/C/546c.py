from collections import deque

def wars():
    n = int(input())
    cards = input().split()
    tot = int(cards[0])
    queue1 = deque(int(i) for i in cards[1:])
    test = queue1
    queue2 = deque(int(i) for i in input().split()[1:])
    c = 0
    while queue1 and queue2:
        if c > 5000:
            return -1
        c1 = queue1.popleft()
        c2 = queue2.popleft()
        c += 1
        if c1 > c2:
            queue1.append(c2)
            queue1.append(c1)
        else:
            queue2.append(c1)
            queue2.append(c2)
    w = '1' if queue1 else '2'
    return str(c) + ' ' + w

print(wars())
