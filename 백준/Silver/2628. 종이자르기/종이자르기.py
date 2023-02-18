w, h = map(int, input().split())
N = int(input())
hs = [0, h]
ws = [0, w]

for _ in range(N):
    dr, num = map(int, input().split())
    if dr == 0:
        hs.append(num)
    elif dr == 1:
        ws.append(num)

hs.sort()
ws.sort()

mx = 0
for i in range(1, len(ws)):
    for j in range(1, len(hs)):
        ww = ws[i] - ws[i - 1]
        hh = hs[j] - hs[j - 1]
        area = ww * hh
        if area > mx:
            mx = area

print(mx)