'''
가능한 모든 경우 처리
n: 교환 횟수

시간 복잡도
6C2 => 15번의 경우의 수
15의 10승
가지치기 필요!
'''

# lst = [8, 8, 8, 3, 2]

def dfs(n):
    global ans

    if n == N:  # 교환횟수
        ans = max(ans, int("".join(map(str, lst))))
        return

    # L개에서 2개 뽑는 모든 조합(들을 교환)
    for i in range(0, L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str, lst)))
            if (n, chk) not in v:
                dfs(n + 1)
                v.append((n, chk))
            
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for tc in range(1, T + 1):
    st, t = input().split()
    N = int(t)  # 교환 횟수
    lst = []
    for ch in st: # 문자열수를 정수로 리스트에 담기
        lst.append(int(ch))
    L = len(lst) # 수 리스트 길이

    ans = 0
    v =[]

    dfs(0)

    print(f'#{tc} {ans}')