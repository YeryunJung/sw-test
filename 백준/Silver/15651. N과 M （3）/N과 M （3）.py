def permutation(n, lst):
    # 종료 조건
    if n == M:
        result.append(lst)
        return
    
    # 하부 함수
    for i in range(1, N + 1):
        permutation(n + 1, lst + [i])
        
        
N, M = map(int, input().split())
result = []

permutation(0, [])
for lst in result:
    print(*lst)