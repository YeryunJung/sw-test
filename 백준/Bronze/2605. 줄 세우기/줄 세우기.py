def line_up(arr, idx, num):  # arr는 현재 사람 배열, i는 현재 사람 인덱스, num은 받은 수
    if num == 0:
        pass
    arr.insert(idx - num, arr[idx])
    del arr[idx + 1]

def add_one(n):
    return n + 1

total = int(input())
nums = list(map(int, input().split()))
line = list(range(total))
for i in range(len(nums)):
    line_up(line, i, nums[i])

line = list(map(add_one, line))

print(*line)