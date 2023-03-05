# 수학여행 참가하는 학생 수 N, 한 방 최대 인원수 K
N, K = map(int, input().split())
boy = [0] * 7
girl = [0] * 7
room = 0
for _ in range(N):
    # 성별 S (여학생 0, 남학생 1)
    # 학년 Y
    S, Y = list(map(int, input().split()))
    # 여학생인 경우
    if S:
        girl[int(Y)] += 1
    # 남학생인 경우
    else:
        boy[int(Y)] += 1

for el in boy:
    if el == 0:
        continue
    if el > K and el % K == 0:
        room += el // K
    elif el > K and el % K != 0:
        room += el // K + 1
    else:
        room += 1

for el in girl:
    if el == 0:
        continue
    if el > K and el % K == 0:
        room += el // K
    elif el > K and el % K != 0:
        room += el // K + 1
    else:
        room += 1
        
print(room)
