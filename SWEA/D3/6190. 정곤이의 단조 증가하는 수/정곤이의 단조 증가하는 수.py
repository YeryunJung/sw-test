T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    candidate = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            num = lst[i] * lst[j]
            num_n = num
            num_list = []
            while num != 0:
                num_list.insert(0, num % 10)
                num = num//10

            result = True
            for k in range(1, len(num_list)):
                if num_list[k] < num_list[k - 1]:
                    result = False
            if result:
                candidate.append(num_n)

    mx = -1
    if len(candidate) >= 1:
        mx = max(candidate)
    print(f'#{tc}', mx)