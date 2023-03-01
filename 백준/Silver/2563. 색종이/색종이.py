N = int(input())
points = []
for _ in range(N):
    w, h = map(int, input().split())
    for i in range(w, w + 10):
        for j in range(h, h + 10):
            points.append((i, j))

result = list(set(points))

print(len(result))