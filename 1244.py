import sys
# 1 켜져있음 / 0 꺼져있음
# 1 이상이고 8 이하인 자연수 나눠줌

# 남학생 == 1
# 스위치 번호가 받은 수의 배수이면 > 상태 바꾼다
# 3을 받았다면 3, 6번 스위치의 상태를 바꾼다

# 여학생 == 2
# 받은 수와 같은 번호 스위치 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간 찾아서 > 상태 바꾼다
# 구간에 속한 스위치 개수는 항상 홀수

# 출력
# 스위치들의 마지막 상태

# a, b = map(int, sys.stdin.readline().split())
# print([list(map(int, data.split())) for data in sys.stdin.readlines()])
# for line in sys.stdin:
#     a, b = map(int, line.split())
#     print(a+b)

switch_num = 8
switch_list = [0, 1, 0, 1, 0, 0, 0, 1]
student_count = 2
input1 = [1, 3]
input2 = [2, 3]


now = input2[1] + 1

# 남학생일 때
if input2[0] == 1:
    for i in range(1, switch_num + 1):
        # 스위치 인덱스가 받은 수의 배수라면
        if i % input2[1] == 0:
          switch_list[i - 1] = 0 if switch_list[i - 1] == 1 else 1
# 여학생일 때
else:
    i = 1
    while True:
        right = switch_list[now + i]
        left = switch_list[now - i]
        if right != left:
            break
        i += 1
    switch_list[now] = 0 if switch_list[now] == 1 else 1
    while i > 1:
      i -= 1
      switch_list[now + i] = 0 if switch_list[now + i] == 1 else 1
      switch_list[now - i] = 0 if switch_list[now - i] == 1 else 1

print(switch_list)