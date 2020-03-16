def shelves_fit(cups, medals, shelves):
    while shelves > 0 and cups > 0 or medals > 0:
        if shelves == 0:
            return "NO"
        if cups > 0:
            cups-=5
            shelves-=1
        elif medals > 0:
            medals-=10
            shelves-=1
    if cups <= 0 and medals <= 0:
        return "YES"
    else:
        return "NO"


def main():
    cups = sum([int(i) for i in input().split()])
    medals = sum([int(i) for i in input().split()])
    shelves = int(input())
    print(shelves_fit(cups,medals,shelves))


main()
