T = 10
for tc in range(1, T + 1):
    length = int(input())
    infix = input()
    stack = []
    result = ''

    # 변환할 식을 순회
    for token in infix:
        # 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token

        # 토큰이 연산자인 경우
        else:
            # stack이 비어있는 경우, stack에 push
            if not stack:  # if len(stack) = 0
                stack.append(token)

            else:
                # incoming 우선순위가 2인 경우
                if token == '*':
                    # stack이 존재하고 stack의 top 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(token)

                # 우선순위가 1인 경우
                elif token == '+':
                    # stack의 top 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    while stack:
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    s = 0
    stack2 = []
    for el in result:
        if el.isdecimal():
            stack2.append(int(el))
        elif el == '*':
            num2 = stack2.pop()
            num1 = stack2.pop()
            stack2.append(num1 * num2)
        elif el == '+':
            num2 = stack2.pop()
            num1 = stack2.pop()
            stack2.append(num1 + num2)

    s = stack2.pop()
    print(f'#{tc} {s}')