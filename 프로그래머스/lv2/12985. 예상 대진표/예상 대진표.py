# 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B
# def solution(n,a,b):
#     i = 0
#     while True:
#         if a % 2 == 1 and b % 2 == 0 and a + 1 == b:
#             break
#         else:
#             if a % 2 == 1:
#                 a = (a + 1) // 2
#             elif a % 2 == 0:
#                 a = a // 2
#             if b % 2 == 1:
#                 b = (b + 1) // 2
#             elif b % 2 == 0:
#                 b = b // 2
#         i += 1
        
#     return i + 1
#########################################
# def solution(n, a, b):
#     a_num = b_num = 0
#     if a % 2 == 1:
#         a_num = (a + 1) // 2
#     elif a % 2 == 0:
#         a_num = a // 2
#     if b % 2 == 1:
#         b_num = (b + 1) // 2
#     elif b % 2 == 0:
#         b_num = b // 2
    
#     print(a_num)
#     print(b_num)
    
#     return b_num - a_num + 1
#########################################
import math

def solution(n, a, b):
    aa = min(a,b)
    bb = max(a,b)
    
    # 몇 제곱인지 찾기
    i = 0 
    nn = n
    while nn != 1:
        nn //= 2
        i += 1
    
    answer = 1
    # mid = n // 2
    while (aa % 2 == 0 or aa + 1 != bb):
        # if aa <= mid and bb <= mid:
        #     answer -= 1
        # elif aa > mid and bb > mid:
        #     answer -= 1
        
        aa = math.ceil(aa / 2)
        bb = math.ceil(bb / 2)
    
        # mid = mid // 2
        answer += 1
    
    return answer

    