n,t = [int(i) for i in input().split()]
books = [int(i) for i in input().split()]
i = 0
j = 0
count = 0
acum = 0
tmp_acum = 0
tmp_count = 0
while i < n:
    if tmp_acum + books[i] <= t:
        tmp_acum += books[i]
        tmp_count += 1
        i += 1
    else:
        count = max(count, tmp_count)
        tmp_acum = max(tmp_acum - books[j], 0)
        tmp_count = max(tmp_count - 1, 0)
        j += 1
        i = max(i, j)
print(str(max(count, tmp_count)))
