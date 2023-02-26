# 들어오는 노드의 좌측과 우측트리를 각각 재귀로 계산
def cal(n):
    if tree[n]:
        if tree[n] == '+':
            return cal(int(left[n])) + cal(int(right[n]))
        elif tree[n] == '-':
            return cal(int(left[n])) - cal(int(right[n]))
        elif tree[n] == '/':
            return cal(int(left[n])) // cal(int(right[n]))
        elif tree[n] == '*':
            return cal(int(left[n])) * cal(int(right[n]))
        else:
            return int(tree[n])

T = 10
for tc in range(1, T + 1):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    tree = [0] * (N + 1)
    detail = []
    for _ in range(N):
        node = input().split()
        detail.append(node)

    for el in detail:
        tree[int(el[0])] = el[1]
        if len(el) > 2:
            left[int(el[0])] = int(el[2])
            right[int(el[0])] = int(el[3])

    result = cal(1)

    print(f'#{tc}', result)