T = int(input())
for tc in range(1, T + 1):
    # 수강생의 수 N, 과제 제출한 사람 수 K
    N, K = map(int, input().split())
    submit_lst = list(map(int, input().split()))
    submit_lst.sort()
    student = list(range(1, N + 1))
    
    # 과제제출자가 아니면 리스트에 추가
    result = []
    for el in student:
        if el not in submit_lst:
            result.append(el)

    print(f'#{tc}', *result)