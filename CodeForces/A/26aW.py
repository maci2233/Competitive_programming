#TIME LIMIT EXCEEDED

import math

def number():
    num = int(input())
    if num < 6:
        return 0
    res=0
    for i in range(6, num+1):
        almost = 0
        for j in range(2, i+1):
            primo = True
            max = math.floor(math.sqrt(j))
            for n in range(2, max+1):
                if j % n == 0:
                    primo = False
                    break
            if primo:
                if i % j == 0:
                    almost = almost+1
                    if almost == 3:
                        break
        if almost == 2:
            res = res+1
    return res

print(str(number()))
