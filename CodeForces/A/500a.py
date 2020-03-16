def check_cell(n,t,portals):
    pos = 1
    i = 0
    while pos < t:
        pos+=portals[i]
        i+=portals[i]
        if pos > t:
            return False
    return True


def main():
    n,t = [int(i) for i in input().split()]
    portals = [int(i) for i in input().split()]
    if check_cell(n,t,portals):
        print("YES")
    else:
        print("NO")


main()
