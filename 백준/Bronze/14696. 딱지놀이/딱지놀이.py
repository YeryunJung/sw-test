T = int(input())
for test_case in range(1, T + 1):
    result = ''
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]

    
    def win():
        for i in range(4, 0, -1):
            if a.count(i) > b.count(i):
                return 'A'
            elif a.count(i) < b.count(i):
                return 'B'
        return 'D'
    result = win()
    # if result == None:
    #     result = 'D' 
    print(result)