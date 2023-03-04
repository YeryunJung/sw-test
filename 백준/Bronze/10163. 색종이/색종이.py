grid = [[0] * 1001 for _ in range(1001)]
N = int(input())
for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for j in range(x, x + w):
        for k in range(y, y + h):
            grid[j][k] = i
            
cnts = [0] * (N + 1)
for lst in grid:
    for el in lst:
        cnts[el] += 1

print(*cnts[1:], sep='\n')