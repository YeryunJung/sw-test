def solution(cap, n, deliveries, pickups):
    
    # 거리와 배달을 zip으로 묶고 enumerate로 1부터의 거리를 가져온다
    # if 문으로 수거할 상자가 있는 경우만 가져온다
    idps = [(i, d, p) for i, (d, p) in enumerate(zip(deliveries, pickups), 1) if d or p]
    # [(1, 1, 0), (2, 0, 3), (3, 3, 0), (4, 1, 4), (5, 2, 0)]
    
    # 얼만큼 배달 / 수거했는지 확인하는 변수
    delivery = 0
    pickup = 0
    answer = 0
    
    # 가장 거리가 먼 집부터 고려
    while idps:
        i, d, p = idps.pop()
        delivery += d
        pickup += p
        # 배달과 수거 중 하나라도 있다면 집까지 이동해서 둘다 0 이하가 될 때까지 이동한디
        while delivery > 0 or pickup > 0:
            # 이동하면서 cap 만큼 배달 수거 작업
            # 음수 값으로 바뀌면 배달 수거 할 수 없다
            delivery -= cap
            pickup -= cap
            answer += 2 * i
            
    return answer