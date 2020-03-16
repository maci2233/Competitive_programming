def main():
    n = int(input())
    res = 0
    for i in range(0,n):
        sol = input().split()
        a = int(sol[0])
        b = int(sol[1])
        c = int(sol[2])
        if a+b+c >= 2:
            res = res + 1
    print(res)

main()
