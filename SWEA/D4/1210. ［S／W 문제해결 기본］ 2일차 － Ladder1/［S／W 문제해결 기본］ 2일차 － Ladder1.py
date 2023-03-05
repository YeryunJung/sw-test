def check(x, y):
    while x != 0:
        # 위쪽 길을 만났을 경우
        if ladder[x - 1][y] == 1 and ladder[x][y - 1] == 0 and ladder[x][y + 1] == 0:
            # 좌우 길을 만날 때까지 위로 가기
            while ladder[x][y - 1] == 0 and ladder[x][y + 1] == 0 and x != 0:
                ladder[x][y] = 0
                x = x - 1
        # 좌측 길을 만났을 경우
        elif ladder[x][y-1] == 1:
            # 좌측에 길이 없어질 때까지 좌측으로 가기
            while ladder[x][y - 1] == 1:
                ladder[x][y] = 0
                y = y - 1
        # 우측 길을 만났을 경우
        elif ladder[x][y+1] == 1:
            # 좌측에 길이 없어질 때까지 좌측으로 가기
            while ladder[x][y + 1] == 1:
                ladder[x][y] = 0
                y = y + 1

    # 한번 더 도달했는지 확인
    if x == 0:
        return y


T = 10
for tc in range(1, T + 1):
    tc_num = int(input())
    # 양옆에 패딩으로 0을 하나씩 붙여줌
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    end = ladder[99].index(2)

    result = check(99, end)

    print(f'#{tc}', result - 1)
