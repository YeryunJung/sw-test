from heapq import heappush, heappop

def recursion(users, emoticons, emoidx, heap):
    if emoidx == len(emoticons):
        sub_buy = [0, 0]  # 구독 서비스 가입자 수, 구매 총액
        for rate, limit in users:
            userbuy = 0
            for price, salerate in emoticons:
                # 각 사용자들은 자신 기준에 따라 일정 비율 이상 할인하는 이모티콘 모두 구매
                if rate <= salerate:
                    userbuy += price * (100 - salerate) // 100  # 가격은 100의 배수
            # 구매 비용 합이 일정 가격 이상이면 이모티콘 서비스 구독
            if limit <= userbuy:
                sub_buy[0] += 1
                userbuy = 0
            sub_buy[1] += userbuy
        # 목표 기준
        # [1, 1], [1, 2], [2, 1], [2, 2]
        # 음수를 붙여서 min heap을 max heap으로 변경
        heappush(heap, [-sub_buy[0], -sub_buy[1]])
    else:
        # 이모티콘마다 할인율은 4개 중 하나로 설정
        for salerate in [10, 20, 30, 40]:
            emoticons[emoidx][1] = salerate
            recursion(users, emoticons, emoidx + 1, heap)

            
def solution(users, emoticons):
    heap = []
    # 가격과 할인율(0 디폴트)
    emoticons = [[price, 0] for price in emoticons]
    recursion(users, emoticons, 0, heap)
    result = heappop(heap)
    return [-result[0], -result[1]]