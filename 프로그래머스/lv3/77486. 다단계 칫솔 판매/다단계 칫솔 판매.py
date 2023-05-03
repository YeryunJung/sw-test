# 똑같이 트리를 형성
# 구성한 트리 안에서 돈이 어떻게 배분되는지 표현
# 트리는 부모 노드로 타고 올라가야 한다
# 이름이 중복되지 않는다고 가정 (조건이 명시되어 있지 않기 때문에)

class Node:
    def __init__(self, parent):
        self.val = 0  # 판매 금액
        self.parent = parent  # 부모 노드

    def divide(self, money):
        # 분배된 이익 (10%)
        divided_money = money // 10
        # 분배된 돈을 뺀 판매액
        self.val += (money - divided_money)
        # 이익금이 0보다 크고 부모가 존재한다면
        # 부모 노드도 배분된 이익금 갱신
        if divided_money > 0 and self.parent:
            self.parent.divide(divided_money)
        
def solution(enroll, referral, seller, amount):
    # 민호는 parent가 없기 때문에 None으로 시작
    center = Node(None)
    n = len(enroll)  # 민호를 제외한 구성원의 수 
    dic = dict()
    dic.update({'-': center})
    
    for i in range(n):
        person = enroll[i]  # 구성원
        parent = referral[i]  # 구성원의 부모노드
        # parent를 부모로 가지는 새로운 노드를 만들어서 딕셔너리에 업데이트
        node = Node(dic[parent])
        dic.update({person: node})

    m = len(seller)  # 판매가 이루어진 횟수
    
    # 각각의 노드마다 판매 금액이 갱신
    for i in range(m):
        seller_name = seller[i]  # 이름이 i번째인 사람
        price = amount[i] * 100  # 그 사람이 낸 수익
        seller_node = dic[seller_name]  # 그 사람의 노드
        seller_node.divide(price)  # 수익금을 갱신
        
    answer = []
    for name in enroll:
        answer.append(dic[name].val)
        
    return answer