def postord(n):
    if n and n <= N:
        postord(n * 2)
        postord(n * 2 + 1)
        infix.append(lst[n])

T = 10
for tc in range(1, T + 1):
    N = int(input())
    detail = []
    for _ in range(N):
        node = input().split()
        detail.append(node)

    lst = [0] * (N + 1)
    for el in detail:
        lst[int(el[0])] = el[1]
    # 후위표현식 배열
    infix = []
    postord(1)

    stack = []
    result = 1
    for el in infix:
        if el.isdigit():
            stack.append(int(el))
        else:
            if len(stack) >= 2:
                op2 = stack.pop()
                op1 = stack.pop()
                if el == '*':
                    stack.append(op1 * op2)
                elif el == '+':
                    stack.append(op1 + op2)
                elif el == '-':
                    stack.append(op2 - op1)
                elif el == '/':
                    if op1 == 0 or op2 == 0:
                        op1 = 1
                        op2 = 1
                    stack.append(op2 // op1)
            else:
                result = 0

    print(f'#{tc}', result)