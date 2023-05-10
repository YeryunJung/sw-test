# def check(word):
#     word = list(word)
#     while True:
#         if len(word) == 0:
#             return 1
#         if len(word) == 1:
#             return 0
#         for i in range(1, len(word)):
#             if word[i - 1] == word[i]:
#                 del word[i - 1]
#                 del word[i - 1]
#                 break
#             if i == len(word) - 1:
#                 return 0

# def check(word):
#     l = len(word)
#     str_list = []
#     while True:
#         if len(word) == 0:
#             return 1
#         if len(word) == 1:
#             return 0
#         for i in range(len(word) - 1, 0, -1):
#             if word[i] == word[i - 1]:
#                 del word[-1]
#                 del word[-1]
#                 break
#             elif word[i] != word[i - 1]:
#                 str_list.append(word[i])
#                 del word[-1]
#         if l == len(word):
#             return 0
#         if len(str_list) >= 2:
#             check(str_list)
            
def check(word):
    l = len(word)
    str_list = []
    
    i = len(word) - 1
    while i >= 0:
        if i >= 1 and word[i] == word[i - 1]:
            del word[-1]
            del word[-1]
            i -= 2
        elif i == 0 or word[i] != word[i - 1]:
            if str_list and str_list[-1] == word[i]:
                del str_list[-1]
                del word[-1]
            else:
                str_list.append(word[i])
                del word[-1]
            i -= 1
            
        # 종료조건
    if len(str_list) == 0:
        return 1
    elif len(str_list) > 0:
        return 0

def solution(s):
    s = list(s)
    answer = check(s)
    
    return answer
    
    return answer