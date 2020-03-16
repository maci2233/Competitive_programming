n = int(input())
books = [int(i) for i in input().split()]
found = set()
b_i = 0
res = ''
for book in [int(i) for i in input().split()]:
    if book in found:
        res += '0 '
    else:
        c = 1
        while books[b_i] != book:
            found.add(books[b_i])
            b_i += 1
            c += 1
        res += str(c) + ' '
        b_i += 1
print(res[:-1])
