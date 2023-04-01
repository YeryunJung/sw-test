'''
암호는 서로 다른 L개의 알파벳 소문자들로 구성
최소 한 개의 모음과 최소 두 개의 자음으로 구성
암호는 알파벳이 증가하는 순서로 배열 abc

암호로 사용했을 문자의 종류는 C
C개의 문자들이 주어졌을 때 가능성 있는 암호를 모두 구하라

아스키코드 97부터 122는 a부터 z를 의미
ord('a')
chr(97)
'''


def dfs(n, lst):
    global vowel, L, C

    # 가지치기 : 입력 조건
    if (3 > L) or (L > C) or (C > 15):
        return

    # 개수가 일치하는 경우
    if n == L:
        # 가지치기 : 모음 자음 개수 확인
        v = c = 0
        for el in lst:
            if el in vowel:
                v += 1
                c = len(lst) - v
        if (v < 1) or (c < 2):
            return
        else:
            result.append(lst)
            return
    else:
        # 정렬된 문자 배열을 순회하면서
        for i in range(C):
            # 리스트가 있으면
            if lst:
                # 방문 확인 및 암호 순서 한번 더 확인
                if visit[i] == 0 and (ord(lst[-1]) < ord(sort_lst[i])):
                    visit[i] = 1
                    dfs(n + 1, lst + [sort_lst[i]])
                    visit[i] = 0
            # 리스트 없으면 방문만 확인
            else:
                if visit[i] == 0:
                    visit[i] = 1
                    dfs(n + 1, lst + [sort_lst[i]])
                    visit[i] = 0


L, C = map(int, input().split())
char = list(input().split())

# 문자를 알파벳 증가하는 순서대로 정렬
sort_lst = []
sort_num = []
for el in char:
    sort_num.append(ord(el))
sort_num.sort()
for el in sort_num:
    sort_lst.append(chr(el))

# 모음 자음 개수 확인용
vowel = ['a', 'e', 'i', 'o', 'u']
# 방문 확인용
visit = [0] * C
result = []

dfs(0, [])
for lst in result:
    print(''.join(lst))
