def check(x, y):
    fly = board[x][y]
    for i in range(4):
        for j in range(1, M):
            ni = x + di[i] * j
            nj = y + dj[i] * j
            if 0<=ni<N and 0<=nj<N:
                fly += board[ni][nj]

    fly2 = board[x][y]
    for i in range(4):
       for j in range(1, M):
           ni = x + dii[i] * j
           nj = y + djj[i] * j
           if 0<=ni<N and 0<=nj<N:
               fly2 += board[ni][nj]

    return max(fly, fly2)


T = int(input())
for tc in range(1, T+1):
    # N 크기의 배열, M 스프레이 세기
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0]*N for _ in range(N)]
    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 대각선
    dii = [-1, -1, 1, 1]
    djj = [-1, 1, -1, 1]

    Max = 0

    for i in range(len(board)):
        for j in range(len(board)):
            Max = max(Max, check(i, j))

    print(f'#{tc}', Max)