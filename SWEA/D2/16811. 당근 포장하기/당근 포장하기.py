T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    minV = 1000
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if lst[i] != lst[i + 1] and lst[j] != lst[j + 1]:
                # 각 그룹의 당근 개수
                    A = i + 1
                    B = j - i
                    C = N - 1 - j
                    if A*B*C != 0 and A<=N//2 and B<=N//2 and C<=N//2:
                        if minV > max(A, B, C) - min(A, B, C):
                            minV = max(A, B, C) - min(A, B, C)
                # if a[-1] != b[0] and b[-1] != c[0]:
                #     if len(a)*len(b)*len(c) != 0 and len(a)<=N//2 and len(b)<=N//2 and len(c)<=N//2:
                #         if minV > max(len(a), len(b), len(c)) - min(len(a), len(b), len(c)):
                #             minV = max(len(a), len(b), len(c)) - min(len(a), len(b), len(c))

    if minV == 1000:
        minV = -1

    print(f'#{tc}', minV)