# 고른 수열은 오름차순이어야 한다.

def permutation(n, lst):
    # 종료 조건 + 정답 처리
    if n == M:
        result.append(lst)
        return

    # 하부 함수 호출
    for i in range(1, N + 1):
        # 현재 리스트가 있을 때
        if lst:
            # 오름차순이고 방문 안한 경우
            if i > lst[-1] and visited[i] == 0:
                visited[i] = 1
                permutation(n + 1, lst + [i])
                visited[i] = 0
        # 현재 리스트가 없을 때
        else:
            if visited[i] == 0:
                visited[i] = 1
                permutation(n + 1, lst + [i])
                visited[i] = 0


N, M = map(int, input().split())
result = []
visited = [0] * (N + 1)

permutation(0, [])
for lst in result:
    print(*lst)
