#07

# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴
nums = [2, 7, 11, 15]
target = 9

# 출력
# [0, 1]

result = []
for i in range(len(nums)):
  for j in range(i + 1, len(nums)):
    if nums[i] + nums[j] == target:
      result += [i, j]
print(result)


# 08

