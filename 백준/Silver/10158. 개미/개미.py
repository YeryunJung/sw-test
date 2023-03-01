# 격자 우측 끝 점 (가로, 세로)
w, h = map(int, input().split())
# 초기 위치값
p, q = map(int, input().split())
# 움직일 시간
t = int(input())
# 출력할 변수 초기화
x = y = 0

w_share = (t + p) // w
# w_remain = (t + p) % w
# 몫이 짝수면
if w_share % 2 == 0:
    x = (t + p) % w
else:
    x = w - (t + p) % w

h_share = (t + q) // h
# h_remain = (t + q) % h
# 몫이 짝수면
if h_share % 2 == 0:
    y = (t + q) % h
else:
    y = h - (t + q) % h

print(x, y)