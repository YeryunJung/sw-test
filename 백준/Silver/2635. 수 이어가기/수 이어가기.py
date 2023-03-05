def keep(n, m):
    memo[0] = n
    memo[1] = m

    j = 2
    while True:
        memo[j] = memo[j - 2] - memo[j - 1]
        if memo[j] < 0:
            return (j, memo)
        j += 1

num = int(input())
half = num//2 + 1
memo = [0] * 30000

mx = 0
mx_lst = 0
for h in range(half, num + 1):
    result = keep(num, h)
    if result[0] >= mx:
        mx = result[0]
        mx_lst = result[1][:]

mx_lst = mx_lst[:mx]

print(mx)
print(*mx_lst)
