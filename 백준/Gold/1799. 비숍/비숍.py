def dfs(n, cnt):
    global ans
    # 현재 까지의 값에 남은 사선 개수를 다 놔도 정답 갱신 안되는 경우
    if ans >= (cnt + L - n):
        return

    if n == L:
        ans = max(ans, cnt)
        return

    for ci, cj in lst[n]:  # 현재 사선 번호에서 가능한 위치 하나씩 놓고 다음 사선으로 이동
        # 대각선에 놓여있는지 확인
        if v[ci-cj] == 0:
            v[ci-cj] = 1
            # 다음 사선 가면서, 개수도 증가
            dfs(n + 1, cnt + 1)
            v[ci-cj] = 0
    dfs(n + 1, cnt)  # 이번 사선에서 안 놓고 다음 사선으로 이동


N = int(input())
board = []
for _ in range(N):
    lst = list(map(int, input().split()))
    board.append(lst)
# 사선 좌표 저장
lst = [[] for _ in range(2 * N)]
# board[i][j] == 1 인 경우, i + j 위치에 append
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            lst[i + j].append((i, j))

L = 2 * N - 1
v = [0] * (2 * N)

ans = 0
dfs(0, 0)
print(ans)