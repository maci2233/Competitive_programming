word = input()
ab1,ab2 = word.find('AB'),word.rfind('AB')
ba1,ba2 = word.find('BA'),word.rfind('BA')
if ab1 != -1 and ba1 != -1:
    if ab2-ba1 > 1 or ba2-ab1 > 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
