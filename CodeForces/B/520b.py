from collections import deque

def best_path(n,m):
    queue = deque()
    visited = set()
    queue.append((n,0))
    while queue:
        curr = queue.popleft()
        val,steps = curr[0],curr[1]
        if val == m:
            return steps
        if val < 1:
            continue
        if val-1 not in visited:
            queue.append((val-1, steps+1))
            visited.add(val-1)
        if val*2 not in visited and val < m:
            queue.append((val*2, steps+1))
            visited.add(val*2)
    return -1


def main():
    n,m = [int(i) for i in input().split()]
    print(str(best_path(n,m)))


main()
