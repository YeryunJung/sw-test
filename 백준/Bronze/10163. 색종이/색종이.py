grid = [[-1] * 1001 for _ in range(1001)]
N = int(input())
for i in range(N):
    x, y, w, h = map(int, input().split())
    for j in range(x, x + w):
        for k in range(y, y + h):
            grid[j][k] = i

for i in range(N):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if grid[j][k] == i:
                cnt+=1

    print(cnt)