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

# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 리턴
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 가장 큰 수를 기준으로 그 다음으로 큰 수를 찾는다
# 큰 수와 그 다음 큰 수 사이의 배열을 확인한다
# (배열 사이의 칸 * 두번째로 큰 수) - (배열 안의 요소들의 합) => 빗물 양
# 가장 큰 수를 제외하고 그 다음으로 큰 수를 기준으로 위를 반복한다

rain_amount = 0
for i in range(1, len(height)):
  for j in range(i + 1, len(height)):
    if height[i] <= height[j] and i + 1 != j:
        col = sum(height[i + 1:j])
        total = (j - i - 1) * height[i]
        rain_amount += total - col
        i = j
    elif height[i] <= height[j] and i + 1 == j:
        i = j
        
        
print(rain_amount)




def trap(self, height):
  stack = []
  volume = 0

  for i in range(len(height)):
    # 스택의 맨 마지막보다 현재 요소가 더 크다면
    # 변곡점을 만나는 경우
    while stack and height[i] > height[stack[-1]]:
      # 스택에서 꺼낸다
      # 스택에서 하나씌 꺼내면서 이전과의 차이만큼 물 높이를 채워 나간다
      top = stack.pop()

      if not len(stack):
        break

      # 이전과의 차이만큼 물 높이 처리
      distance = i - stack[-1] - 1
      waters = min(height[i], height[stack[-1]] - height[top])

      volume += distance * waters

    stack.append(i)
  return volume





