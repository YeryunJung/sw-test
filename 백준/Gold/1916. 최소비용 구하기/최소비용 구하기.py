import heapq

# 도시의 개수 N(1 ≤ N ≤ 1,000)
N = int(input())
# 버스의 개수 M(1 ≤ M ≤ 100,000)
M = int(input())
INF = int(1e9)
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # 출발 도시번호, 도착 도시번호, 버스 비용
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
# 출발점의 도시번호와 도착점의 도시번호
s_city, e_city = map(int, input().split())

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

dijkstra(s_city)

# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력
print(distance[e_city])
