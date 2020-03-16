def is_same(s1, s2):
    n = len(s1)
    m = len(s2)
    if n != m:
        return False
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    if s1 == s2:
        return True
    else:
        return False


def main():
    name = input() + input()
    check = input()
    print("YES") if is_same(name, check) else print("NO")


main()
