T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    lst = [0] + list(map(int, input().split()))

    s = [0] * 13
    for i in range(1, 13):
        # 가능한 방법 중 i달 까지의 최소비용 갱신
        s[i] = s[i - 1] + price[0] * lst[i]  # 일간권
        s[i] = min(s[i], s[i - 1] + price[1])  # 월간권
        if i >= 3:
            s[i] = min(s[i], s[i - 3] + price[2])  # 분기권
        if i >= 12:
            s[i] = min(s[i], s[i - 12] + price[3])  # 연간권

    ans = s[12]

    print(f'#{tc} {ans}')