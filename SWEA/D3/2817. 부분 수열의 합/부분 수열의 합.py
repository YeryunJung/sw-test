def dfs(n, lst, sm):  # n은 배열의 인덱스 (사용할 거냐 하지 않을 거냐)
    global result

    # 가지치기 : 여태까지의 합이 K 보다 커졌다면 종료
    if K < sm:
        return

    if n == N:  # 트리의 끝까지 왔을 때
        if sm == K:
            result.append(lst)
        return

    dfs(n + 1, lst + [A[n]], sm + A[n])
    dfs(n + 1, lst, sm)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = []
    dfs(0, [], 0)

    cnt = len(result)
    print(f'#{tc} {cnt}')

