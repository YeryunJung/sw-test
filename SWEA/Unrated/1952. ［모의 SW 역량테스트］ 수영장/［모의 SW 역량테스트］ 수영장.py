def dfs(n, sm): # n이 깊이(월), sm이 비용
    global ans

    # 가지치기 : 현재의 정답보다 sm이 더 커졌으면 종료
    if ans <= sm:
        return

    # 12월 넘어가면 종료
    if n > 12:
        ans = min(ans, sm)
        return

    # 하부 함수 호출 4개
    dfs(n + 1, sm + price[0] * lst[n])  # 일간권
    dfs(n + 1, sm + price[1])  # 월간권
    dfs(n + 3, sm + price[2])  # 분기권
    dfs(n + 12, sm + price[3])  # 연간권


T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    lst = [0] + list(map(int, input().split()))
    ans = 3000 * 365

    dfs(1, 0)
    print(f'#{tc} {ans}')