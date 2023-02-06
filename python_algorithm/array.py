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


###################################################################

# 현재 위치 i가 더 높으면 물이 찰 수 있다는 것으로 간주한다
# stack을 뽑아 top에 넣는다

def trap(height):
  stack = [] # height의 인덱스들이 들어감
  volume = 0 # 빗물의 양

  for i in range(len(height)): 
    # 변곡점을 만나는 경우
    # 스택이 존재하는 상태에서
    # 스택의 맨 마지막보다 현재 기둥이 더 높다면 > 빗물 고임
    while stack and height[i] > height[stack[-1]]:
      # 변곡점을 만날 때마다 stack에서 하나씩 꺼낸다
      top = stack.pop() # 바로 전의 인덱스 값을 꺼내 top에 할당

      # 스택에 아무것도 없는 상태라면 break
      # 왼쪽 부분에 벽이 없으면 고일 수가 없다
      if not len(stack):
        break

      # 빗물이 고인 바닥 개수
      # 현재 위치(i)에서 스택의 마지막을 뺀 뒤 -1
      distance = i - stack[-1] - 1
      # 양쪽 벽 사이에 물이 들어갈 곳을 구한 것
      # 현재 높이, 스택 마지막의 높이에서 top을 뺀것 중 작은 것
      waters = min(height[i], height[stack[-1]]) - height[top]

      volume += distance * waters

    stack.append(i)
  return volume

##################################################################

def trap(height):
  n = len(height) # 길이

  if n == 0: # 예외처리
    return 0

  lmax = [0] * n # 0으로 가득찬 배열
  rmax = [0] * n # 0으로 가득찬 배열

  lmax[0] = height[0] 
  rmax[n-1] = height[n-1]

  for i in range(i, n):
    # 바로 전의 값과 현재 중 max 값
    lmax[i] = max(lmax[i-1], height[i])

  for i in range(n-2, -1, -1):
    # 오른쪽부터 두개씩 비교하면서 max 값
    rmax[i] = max(rmax[i+1], height[i])
  
  water = 0
  for i in range(n):
    # 두 레이저를 쏜 곳의 음영진 부분의 최솟값
    water += min(lmax[i], rmax[i]) - height[i]

  return water
