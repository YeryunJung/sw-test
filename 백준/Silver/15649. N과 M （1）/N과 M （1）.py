def permutation(n, lst):
    # 종료 조건 + 정답 처리
    if n == M:
        result.append(lst)
        return

    # 하부 함수 호출
    for i in range(1, N+1):
        if visited[i] == 0: # 선택 안한 경우
            visited[i] = 1
            permutation(n + 1, lst+[i])
            visited[i] = 0

# (1 ≤ M ≤ N ≤ 8)
N, M = map(int, (input().split()))
result = [] # 정답 저장용
visited = [0] * (N + 1) # 중복 확인용

permutation(0, [])
for lst in result:
    print(*lst)