def solution(lottos, win_nums):
    answer = []
    mx = mn = 0
    adding_list = list(set(lottos + win_nums))
    if 0 in lottos:
        n_lottos = list(set(lottos))
        zero_nums = 6 - len(n_lottos) + 1
        dupli_num = 12 - len(adding_list) - zero_nums + 1
    else:
        zero_nums = 0
        dupli_num = 12 - len(adding_list) - zero_nums
    
    if dupli_num == 6:
        mx = mn = 1
    elif zero_nums == 6:
        mx = 1
        mn = 6
    elif dupli_num == 0 and zero_nums == 0:
        mx = mn = 6
    else:
        # 최대 당첨
        mx = 7 - (dupli_num + zero_nums)
        # 최소 당첨
        mn = 7 - dupli_num
        
    return [mx, mn]