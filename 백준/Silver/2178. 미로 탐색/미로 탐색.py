def bfs(x, y):
    q = [(x, y)]
    board[x][y] = 0

    while q:
        si, sj = q.pop(0)
        # 네 방향으로 돌면서 
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            # 범위 내, 길이 있는 곳을 새 좌표로 지정
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 1:
                # 목표지점 도달시 1증가 시켜주고 리턴
                if ni == N-1 and nj == M-1:
                    checked[ni][nj] = checked[si][sj] + 1
                    return
                # 길이 있는 곳 좌표 다시 큐에 추가
                q.append((ni, nj))
                # 갔던 곳은 0으로 재할당
                board[ni][nj] = 0
                # 이전 칸의 개수보다 1 증가
                checked[ni][nj] = checked[si][sj] + 1


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
checked = [[0] * M for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

bfs(0, 0)
print(max(map(max, checked)) + 1)