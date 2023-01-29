import sys
# 1 켜져있음 / 0 꺼져있음
# 1 이상이고 8 이하인 자연수 나눠줌

# 남학생 == 1
# 스위치 번호가 받은 수의 배수이면 > 상태 바꾼다
# 3을 받았다면 3, 6번 스위치의 상태를 바꾼다

# 여학생 == 2
# 받은 수와 같은 번호 스위치 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간 찾아서 > 상태 바꾼다
# 구간에 속한 스위치 개수는 항상 홀수

# 입력
# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3

# 출력
# 스위치들의 마지막 상태

def change_switch(idx):
  switch_list[idx] = 0 if switch_list[idx] == 1 else 1

switch_num = int(input())
switch_list = list(map(int, input().split()))
student_count = int(input())
for _ in range(student_count):
  gender, num = map(int, input().split())
  # 남학생일 때
  if gender == 1:
      for i in range(1, switch_num + 1):
          # 스위치 인덱스가 받은 수의 배수라면
          if i % num == 0:
            change_switch(i - 1)
# 여학생일 때
  else:
      now = num + 1
      i = 1
      while True:
          right = switch_list[now + i]
          left = switch_list[now - i]
          if right != left:
              break
          i += 1
      change_switch(now)
      while i > 1:
        i -= 1
        change_switch(now + 1)
        change_switch(now - 1)
print(switch_list)