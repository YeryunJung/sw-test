for _ in range(4):
    si1, sj1, ei1, ej1, si2, sj2, ei2, ej2 = map(int, input().split())

    # 완전히 분리된 경우
    if ei1 < si2 or sj1 > ej2 or ei2 < si1 or sj2 > ej1:
        print('d')
    # 세로 선분이 겹치는 경우
    elif ei1 == si2 or si1 == ei2:
        # 가로까지 겹치는 경우 점
        if sj1 == ej2 or ej1 == sj2:
            print('c')
        # 가로까지는 안겹치면 선분
        else:
            print('b')
    # 가로 선분만 겹치는 경우 선분
    elif sj1 == ej2 or ej1 == sj2:
        print('b')
    # 그외의 것들은 직사각형
    else:
        print('a')