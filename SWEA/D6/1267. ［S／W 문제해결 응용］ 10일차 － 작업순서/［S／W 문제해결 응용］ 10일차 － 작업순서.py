T = 10
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [True for _ in range(v + 1)]
    # 노드와 간선의 리스트
    temp_list = list(map(int, input().split()))
    count = v
    # 선행 순서이므로 반대로 넣어줌
    # a = 1, b = 2 일 경우
    # 2는 1이 수행완료 되어야 가능하다
    for i in range(0, len(temp_list), 2):
        v, e = temp_list[i], temp_list[i + 1]
        graph[e].append(v)
    # 결과누적 리스트
    result = []
    # 노드가 모두 수행될때까지 반복
    while count:
        # 1번부터 마지막 노드까지 반복
        for i in range(1, len(graph)):
            # 현재 노드가 수행되지 않았다면 (True가 수행되지 않은것)
            if visited[i]:
                # 선행 노드를 확인
                for j in graph[i]:
                    # 선행노드가 수행되지 않았다면 멈추고 빠져나와서 다음 노드 확인
                    if visited[j]:
                        break
                    # 선행노드가 수행되었다면
                    # 현재노드 수행했다고 바꾸고 결과에 추가
                    # 노드 수행되었으므로 count 감소
                else: # graph가 빈 요소이면 (선행될 것이 없으면) (for else 문)
                    visited[i] = False
                    result.append(i)
                    count -= 1

    print(f'#{tc}', *result)