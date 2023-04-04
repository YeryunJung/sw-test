def find_mn(team):
    power = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i == j:
                continue
            else:
                power += S[team[i]][team[j]]
    return power


def permutaion(n, lst):
    if n == N/2:
        team1.append(lst)
        team2.append(list(set(member) - set(lst)))
        return

    for i in range(1, N + 1):
        if lst:
            if lst[-1] < i and visited[i] == 0:
                visited[i] = 1
                permutaion(n + 1, lst + [i])
                visited[i] = 0
        else:
            if visited[i] == 0:
                visited[i] = 1
                permutaion(n + 1, lst + [i])
                visited[i] = 0


N = int(input())
member = list(range(1, N + 1))
S = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N + 1)

team1 = []
team2 = []

permutaion(0, [])
ans = 100 * N

for k in range(len(team1)):
    team1_power = find_mn(team1[k])
    team2_power = find_mn(team2[k])
    if team1_power > team2_power:
        ans = min(ans, (team1_power - team2_power))
    elif team2_power > team1_power:
        ans = min(ans, (team2_power - team1_power))
    elif team1_power == team2_power:
        ans = min(ans, 0)

print(ans)