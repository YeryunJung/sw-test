def permutation(n, lst):
    if n == M:
        result.append(lst)
        return

    for i in range(1, N + 1):
        if len(lst) > 0 and i >= lst[-1]:
            permutation(n + 1, lst + [i])
        elif len(lst) == 0:
            permutation(n + 1, lst + [i])


N, M = map(int, input().split())
result = []

permutation(0, [])
for lst in result:
    print(*lst)


