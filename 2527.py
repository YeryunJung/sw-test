
# data = []
n = 4
for _ in range(n):
  x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
  # 겹치는 부분이 없을 때
  if max(x1, x2) < min(p1, p2) and max(y1, y2) < min(q1, q2):
    print('a')
  elif x1 == p2:
    if y1 == q2:
      print('c')
    else:
      print('b')
  elif p1 == x2:
    if y1 == q2:
      print('c')
    else:
      print('b')
  else:
    print('d')
  
  
    # data.append(list(map(int, input().split())))
# data의 각 요소에서
# 0, 1 은 좌측 하단 꼭짓점, 2, 3 은 우상단 꼭짓점


# 꼭짓점을 다 배열에 넣어버리고 중복 처리를 해볼까?

# print(data)

# def check_common_part(data):
#     for square in data:
#         first_left = square[0]
#         first_right = square[2]
#         first_top = square[3]
#         first_bottom = square[1]

#         second_left = square[4]
#         second_right = square[6]
#         second_top = square[7]
#         second_bottom = square[5]

#         first_point = []
#         second_point = []
#         for i in range(first_left, first_right + 1):
#             for j in range(first_bottom, first_top + 1):
#                 first_point.append((i, j))

#         for i in range(second_left, second_right + 1):
#             for j in range(second_bottom, second_top + 1):
#                 second_point.append((i, j))

#         duplicated_list = list(set(first_point).intersection(second_point))

#         result = ''
#         if len(duplicated_list) == 0:
#             print('d')
#         elif len(duplicated_list) == 1:
#             print('c')
#         elif True:
#             for el in duplicated_list:
#                 if duplicated_list[0][0] not in el and duplicated_list[0][1] not in el:
#                     result = 'a'
#         else: 
#             print('b')
        


# print(check_common_part(data))
