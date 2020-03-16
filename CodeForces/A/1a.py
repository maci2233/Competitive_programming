import math

def main():
    str = input().split()
    n = int(str[0])
    m = int(str[1])
    a = int(str[2])
    res = math.ceil(n/a)*math.ceil(m/a)
    print(res)

main()
