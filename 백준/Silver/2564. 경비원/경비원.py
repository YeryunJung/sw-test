def cal_distance(dr, num):
    if dr == 1:
        return num
    elif dr == 3:
        return w + h + w + (h - num)
    elif dr == 2:
        return w + h + (w - num)
    elif dr == 4:
        return w + num

w, h = map(int, input().split())
total = int(input())
store = []
for _ in range(total):
    dr, num = map(int, input().split())
    store.append([dr, num])
my_dr, my_num = map(int, input().split())
my_distance = cal_distance(my_dr, my_num)

block = (w + h) * 2
result = 0
for el in store:
    distance = min(block - (abs(cal_distance(el[0], el[1]) - my_distance)), abs(cal_distance(el[0], el[1]) - my_distance))
    result += distance

print(result)