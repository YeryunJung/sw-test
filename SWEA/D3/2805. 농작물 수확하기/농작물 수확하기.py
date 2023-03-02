T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    center = [N//2, N//2]
    Sum = 0

    for i in range(N):
        for j in range(N):
            if abs(i - center[0]) + abs(j - center[1]) <= N//2:
                Sum += farm[i][j]

    print(f'#{tc}', Sum)