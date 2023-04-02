# [1] 전체 배열 순회 (시작점: si, sj), 사각형
# 자기자리에 되돌아 오는 경우(중복 x, v[] -> len)
# 선택: 직진, 좌회전
# n: 꺽는 횟수 (방향)
# 정답처리 : n == 3 & 시작지점 복귀

di = [1, 1, -1, -1, 1]
dj = [-1, 1, 1, -1, -1]

def dfs(n, ci, cj, v):
    global ans

    # 무조건 종료
    if n > 3:
        return

    # 정답처리
    if n == 3 and (si, sj) == (ci, cj):
        ans = max(ans, len(v))
        return

    # n은 방향, n과 n + 1 꺾고, 안꺾고
    for k in range(n, n + 2):
        ni, nj = ci + di[k], cj + dj[k]
        # 범위 내, 중복 되지 않으면
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(k, ni, nj, v) # 방향, 갈 좌표, 디저트 종류 배열
            v.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    # for si in range(N - 2):
    for si in range(N):
        for sj in range(1, N - 1):
            dfs(0, si, sj, [])

    print(f'#{tc} {ans}')