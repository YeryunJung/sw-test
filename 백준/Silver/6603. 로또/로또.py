def dfs(n, llst):
    if n == 6:
        result.append(llst)
        return
    else:
        for i in range(k):
            # 리스트가 있으면
            if llst:
                # 오름차순이고 방문 안한 요소를 선택
                if S[i] > llst[-1] and v[i] == 0:
                    v[i] = 1
                    dfs(n + 1, llst + [S[i]])
                    v[i] = 0
            # 리스트 없으면 방문 안한 요소를 선택
            else:
                if v[i] == 0:
                    v[i] = 1
                    dfs(n + 1, llst + [S[i]])
                    v[i] = 0


while True:
    lst = list(map(int, input().split()))
    result = []
    # 마지막 줄이면 입력 받기 종료
    if lst == 0:
        break
    k, S = lst[0], lst[1:]
    if (k < 7) or (S[-1] > 49):
        break
    # 방문 검사 리스트
    v = [0] * k

    dfs(0, [])

    for el in result:
        print(*el)
    print()

