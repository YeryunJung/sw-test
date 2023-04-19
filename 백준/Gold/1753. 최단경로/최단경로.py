import sys


import heapq

# 정점의 개수 V와 간선의 개수 E
V, E = map(int, input().split())
# 시작 정점의 번호 K
K = int(input())
INF = int(1e9)
distance = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    # 각 간선을 나타내는 세 개의 정수 (u, v, w)
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작노드 정보를 우선순위 큐에 삽입
    distance[start] = 0  # 시작노드 -> 시작노드 거리 기록
    while q:
        dist, node = heapq.heappop(q)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(방문한 셀) 무시
        if distance[node] < dist:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in graph[node]:
            cost = distance[node] + next[1]  # 시작 -> node 거리 + node -> node의 인접노드 거리
            if cost < distance[next[0]]:  # cost < 시작 -> node의 인접노드 거리
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(K)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
