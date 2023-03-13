# # 최소 개수를 붙여야 하니까 가장 큰 색종이부터 부착 시도
# def put_paper(x, y):
#     flag = False
#     size = 0
#     for k in range(5, 0, -1):
#         if flag:
#             for m in range(x, x + k):
#                 for n in range(y, y + k):
#                     my_board[m][n] = 1
#             return k
#         # # 아무것도 맞는 색종이가 없었으면
#         # else:
#         #     return -1
#
#         # if flag:
#         #     flag = False
#         # else:
#         #     size = k
#         #     break
#         for i in range(x, x + k):
#             # 색종이가 맞지 않아서 끝낸다 > 더 작은 색종이를 붙인다
#             if flag:
#                 break
#             for j in range(y, y + k):
#                 # 색종이가 맞지 않으면 끝낸다 > 더 작은 색종이를 붙인다
#                 if board[i][j] != 1:
#                     flag = True
#                     break
#             # 색종이 크기가 맞았다면
#             else:
#                 flag = False
#     # 색종이가 맞았으면
#     # if not flag:
#     #     for m in range(x, x + size):
#     #         for n in range(y, y + size):
#     #             my_board[m][n] = 1
#     #     return size
#     # # 아무것도 맞는 색종이가 없었으면
#     # else:
#     #     return -1
#
#
# board = [list(map(int, input().split())) for _ in range(10)]
# my_board = [[0] * 10 for _ in range(10)]
#
# result = []
# for i in range(10):
#     for j in range(10):
#         # 색종이 붙일 자리가 있고 이미 붙이지 않았다면
#         if board[i][j] == 1 and my_board[i][j] != 1:
#             result.append(put_paper(i, j))
#
# print(result)

# (r, c)를 기준으로 붙일 수 있는 색종이의 최대 크기를 구하는 함수
def check_size(r, c):
    global board
    res = 1

    # 1씩 4까지 키워나가면서
    for d in range(1, 5):
        # 붙였을 때 9보다 크면
        if r + d > 9 or c + d > 9:
            # 종료
            break

        # 크지 9와 같거나 크지 않다면
        size_up = True
        # 색종이 붙인 부분의 행에서
        for row in board[r:r+d+1]:
            # 붙인 부분의 열 부분이 모두 1이 아니라면
            if row[c:c+d+1] != ['1' for _ in range(d + 1)]:
                # 사이즈 업 x 하고 종료
                size_up = False
                break
        # 사이즈 업이라면 res 1 증가
        if size_up:
            res += 1
        else:
            break

    return res

# board에서 (r, c)를 기준으로 size만큼의 정사각형 범위를 num으로 채우는 함수
def fill(r, c, size, num):
    global board

    # 사이즈 만큼 num으로 재할당
    for rr in range(r, r + size):
        for cc in range(c, c + size):
            board[rr][cc] = num

# depth번째 1이 적힌 칸을 채우는 함수
def backtracking(depth, cnt):
    global board, paper, fill_area, min_cnt

    # 마지막칸까지 채우면 최소 색종이 개수 갱신
    if depth == len(fill_area):
        min_cnt = min(min_cnt, cnt)
        return

    # 지금까지 구한 최소 색종이 개수보다 커지면 종료
    if cnt >= min_cnt:
        return

    r, c = fill_area[depth]
    # 이전 칸에 의해 이미 채워졌으면 다음칸으로 건너뛰기
    if board[r][c] == '0':
        backtracking(depth + 1, cnt)
        return
    size = check_size(r, c)

    # 내가 색종이를 아직 가지고 있다면
    # 0으로 채워주고(색종이 붙여주고) 색종이 개수 차감
    for s in range(size, 0, -1):
        if paper[s] > 0:
            fill(r, c, s, '0')
            paper[s] -= 1
            backtracking(depth + 1, cnt + 1)
            fill(r, c, s, '1')
            paper[s] += 1

def fill_board():
    global board, min_cnt

    backtracking(0, 0)

    # 붙일 수 있는 개수를 넘어갔다면 -1 리턴
    if min_cnt == 30:
        return -1

    return min_cnt

board = []
paper = [0, 5, 5, 5, 5, 5]
fill_area = []
min_cnt = 30

for r in range(10):
    tmp = input().split()
    board.append(tmp)
    for c in range(10):
        if tmp[c] == '1':
            fill_area.append((r, c))

print(fill_board())

