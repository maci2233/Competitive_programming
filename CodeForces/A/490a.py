def main():
    n = int(input())
    studs = [int(i) for i in input().split()]
    st1 = []
    st2 = []
    st3 = []
    for i in range(n):
        if studs[i] == 1:
            st1.append(i+1)
        elif studs[i] == 2:
            st2.append(i+1)
        else:
            st3.append(i+1)
    num = min(len(st1), len(st2), len(st3))
    print(str(num))
    if num > 0:
        for i in range(num):
            team = str(st1[i]) + " " + str(st2[i]) + " " + str(st3[i])
            print(team)


main()
