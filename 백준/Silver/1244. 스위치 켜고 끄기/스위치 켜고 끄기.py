# 스위치 개수
switch_num = int(input())
lst = list(map(int, input().split()))
# 학생 수
student_num = int(input())
for _ in range(student_num):
    # 성별, 받은 숫자
    gender, num = map(int, input().split())
    # 남학생일 경우
    if gender == 1:
        for i in range(len(lst)):
            if (i + 1) % num == 0:
                if lst[i] == 1:
                    lst[i] = 0
                else:
                    lst[i] = 1
    # 여학생일 경우
    elif gender == 2:
        if lst[num - 1] == 1:
            lst[num - 1] = 0
        else:
            lst[num - 1] = 1
        for i in range(1, len(lst)):
            if 0<=num - 1 - i<len(lst) and 0<=num - 1 + i<len(lst):
                if lst[num - 1 - i] == lst[num - 1 + i]:
                    if lst[num - 1 - i] == 1:
                        lst[num - 1 - i] = 0
                    else:
                        lst[num - 1 - i] = 1
                    if lst[num - 1 + i] == 1:
                        lst[num - 1 + i] = 0
                    else:
                        lst[num - 1 + i] = 1
                else:
                    break
            else:
                break

for i in range(0, len(lst), 20):
    print(*lst[i:i+20])