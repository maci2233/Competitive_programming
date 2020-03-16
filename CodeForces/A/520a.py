def is_pangram(word):
    letters = set()
    for e in word:
        letters.add(e.lower())
    if len(letters) == 26:
        return True
    return False


def main():
    n = int(input())
    if n < 26:
        print("NO")
    else:
        word = input()
        if is_pangram(word):
            print("YES")
        else:
            print("NO")

main()
