melon_num = int(input())
w = []
h = []
lengths = []
for _ in range(6):
    dr, length = map(int, input().split())
    lengths.append(length)
    if dr == 1 or dr == 2:
        w.append(length)
    elif dr == 3 or dr == 4:
        h.append(length)

width = max(w)
height = max(h)
area = width * height
three_times_area = area * 3

Sum = 0
for i in range(1, len(lengths)):
    Sum += lengths[i] * lengths[i - 1]
Sum += lengths[-1] * lengths[0]

temp = three_times_area - Sum
print((area - temp) * melon_num)
