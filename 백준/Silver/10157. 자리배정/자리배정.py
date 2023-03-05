# 공연장 크기 가로로 C, 세로로 R
C, R = map(int, input().split())
# 관객의 좌석번호
K = int(input())
# 좌석 배정안되는 경우 0
board = [[0] * C for _ in range(R)]
# 아래 우측 위 좌측
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

cnt = 1
result = i = j = dr = 0
if R * C < K:
    print(0)
    exit()
    
board[i][j] = cnt

while cnt < K:
    ni = i + di[dr]
    nj = j + dj[dr]
    if 0<=ni<R and 0<=nj<C and board[ni][nj] == 0:
        i = ni
        j = nj
        cnt += 1
        board[i][j] = cnt
    else:
        dr = (dr + 1) % 4

if cnt == K:
    result = [j + 1, i + 1]
    print(*result)