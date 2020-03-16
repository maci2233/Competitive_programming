def colors(n):
    for _ in range(n):
        test = [i for i in input().split()]
        for e in test:
            if e == "C" or e == "M" or e == "Y":
                return "#Color"
    return "#Black&White"


def main():
    n,m = [int(i) for i in input().split()]
    print(colors(n))


main()
