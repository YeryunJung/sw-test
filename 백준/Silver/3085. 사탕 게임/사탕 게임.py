"""
가능한 모든 교환 후 최대길이 갱신
모든 교환이 아니라
오른쪽과 아래쪽 교환 후 최대길이
"""
def count(lst):
    cnt = ans = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1
    return ans

def solve(arr):
    mx = 0
    for i in range(N - 1): # 아래 패딩 줄이랑은 교환할 필요가 없어서 N-1 행 까지만
        for j in range(0, N):
            # 오른쪽 사탕과 교환
            # 같을 때 교환해도 상관 없음
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            mx = max(mx, count(arr[i]))
            # 원상복귀
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

            # 아래쪽 사탕과 교환
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            mx = max(mx, count(arr[i]), count(arr[i + 1]))
            # 원상복귀
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

    return mx

N = int(input())
# 오른쪽과 아래에 패딩 주기
arr = [list(input())+[0] for _ in range(N)] + [[0] * (N + 1)]
arr_t = list(map(list, zip(*arr)))

# 가장 긴 연속 부분인 행 체크, 가장 긴 연속 부분인 열 체크 (전치행렬)
ans = max(solve(arr), solve(arr_t))
print(ans)