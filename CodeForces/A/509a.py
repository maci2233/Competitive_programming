def matrix(n):
    if n == 1:
        return 1
    nums = [[1]*n]*n
    for i in range(1,n):
        for j in range(1,n):
            nums[i][j] = nums[i-1][j] + nums[i][j-1]
    return nums[n-1][n-1]


def main():
    n = int(input())
    print(str(matrix(n)))


main()
