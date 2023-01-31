# 입력
# 수열의 길이 N
# N개의 숫자가 빈칸을 사이에 두고 주어짐
# (N은 1 이상 100,000 이하 정수)

# 그 수열 안에서 연속해서 커지거나(같은 것 포함), 
# 혹은 연속해서 작아지는(같은 것 포함) 수열 중 
# 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램

# 출력
# 8

total = int(input())
num_list = list(map(int, input().split(' ')))
# 4 1 3 3 2 2 9 2 3

prev = ''
start = 0
last = 1

arr = []
for i in range(1, total):
  if num_list[i - 1] < num_list[i]:
    arr.append(num_list[i - 1] - num_list[i])


# for i in range(1, total):
#   if num_list[i - 1] < num_list[i]:
#     arr.append('down')
#   elif num_list[i - 1] > num_list[i]:
#     arr.append('up')
#   else: 
#     arr.append('equal')

# for i in range(1, len(arr)):
#   if arr[i - 1] != arr[i]:
#     i += 1
#     start = i
#     last = i + 1
#   elif arr[i - 1] == arr[i]:
#     last += 1
#   elif 'equal' in arr[i - 1] or arr[i]:
#     last += 1
    

# # 앞과 뒤 상태 체크
# def check_sequence(status):
#     global start
#     global last
#     if prev == '':
#         return
#     # 앞과 뒤 상태 다를 경우
#     elif prev != 'equal' and prev != status:
#         start = i
#         last = i + 1
#     elif prev == 'equal' and prev != status:
#         last = i + 1
#     # 앞과 뒤 상태 같을 경우
#     else:
#         last += 1

# for i in range(total):
#     if num_list[i + 1] > num_list[i]:
#         check_sequence('up')
#         prev = 'up'
#         i += 1
#     elif num_list[i + 1] < num_list[i]:
#         check_sequence('down')
#         prev = 'down'
#         i += 1
#     elif num_list[i + 1] == num_list[i]:
#         prev += 'equal'
#         i += 1
#         last += 1
        
