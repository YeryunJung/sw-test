N = 5
board = [list(map(int, input().split())) for _ in range(N)]
nums = []
for _ in range(N):
    nums += (map(int, input().split()))
# 불렸는지 체크하는 배열
checked = [[0] * N for _ in range(5)]

bingo_num = []
# 부르는 수의 좌표 위치 bingo_num 배열에 넣기
for k in range(len(nums)):
    bingo_num += [(i, j) for i in range(5) for j in range(5) if board[i][j] == nums[k]]

def check_bingo():
    global bingo_cnt
    left_diagonal = True
    right_diagonal = True
    for lst in checked:
        if lst.count(1) == N: # 한 줄에 5개면
            bingo_cnt += 1 # 빙고 1번
    # 세로 체크하는 부분
    checked_T = list(map(list, zip(*checked)))
    for lst in checked_T:
        if lst.count(1) == N:
            bingo_cnt += 1
    for i, j in ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4)):
        if checked[i][j] == 0:
            left_diagonal = False
    for i, j in ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0)):
        if checked[i][j] == 0:
            right_diagonal = False
    if left_diagonal:
        bingo_cnt += 1
    if right_diagonal:
        bingo_cnt += 1

result = 1

for position in bingo_num:
    # checked 배열에 1로 체크
    checked[position[0]][position[1]] = 1
    bingo_cnt = 0
    check_bingo()
    # 빙고가 3번 불렸다면
    if bingo_cnt >= 3:
        # 몇 번째 숫자를 불렀을 때인지 출력
        result += bingo_num.index(position)
        break

print(result)