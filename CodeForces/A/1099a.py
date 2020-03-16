snow = [int(i) for i in input().split()]
s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
while snow[1] > 0:
    snow[0] += snow[1]
    if snow[1] == s1[1]:
        snow[0] -= s1[0]
    if snow[1] == s2[1]:
        snow[0] -= s2[0]
    if snow[0] < 0:
        snow[0] = 0
    snow[1] -= 1
print(snow[0])
