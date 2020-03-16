from collections import deque

def inc_level_sons(emp):
    queue = deque()
    queue.append(emp)
    while queue:
        emp = queue.popleft()
        for e in emps[emp]:
            emps_level[e] = emps_level[emp]+1
            queue.append(e)

n = int(input())
emps = [[] for i in range(2005)]
emps_level = [1] * 2005
for i in range(n):
    e = int(input())
    if e != -1:
        emps[e].append(i+1)
        emps_level[i+1] = emps_level[e] + 1
        inc_level_sons(i+1)
print(str(max(emps_level)))
