T = 10
for tc in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 초기값
    mn = 100 * 100

    for sj in range(1, 101):
        # 시작 좌표가 0이면 지나침
        if arr[0][sj] == 0:
            continue

        # 시작좌표를 현재좌표에 할당
        cj = sj
        cnt = dr = ci = 0

        while ci < 99:
            # 한번 더 갈 때 카운트 증가
            cnt += 1
            # 방향이 아래면
            if dr == 0:
                # 아래로 이동
                ci += 1
                # 왼쪽에 길이 있다면 방향 왼쪽으로 변환
                if arr[ci][cj - 1] == 1:
                    dr = -1
                # 오른쪽에 길이 있다면 방향 오른쪽으로 변환
                elif arr[ci][cj + 1] == 1:
                    dr = 1
            # 방향이 아래가 아니라면
            else:
                cj += dr
                # 그 다음 방향에 0이 있다면
                if arr[ci][cj + dr] == 0:
                    dr = 0

        # 정답 갱신
        if mn >= cnt:
            mn, ans = cnt, sj - 1

    print(f'#{tc}', ans)