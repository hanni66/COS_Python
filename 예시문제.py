def solution(a, b):
    count = 0
    for i in a:
        if not i in b:
            count += 1
            print(i)
    return count

# 우산이 없어 비를 맞은 날은 언제인가?     
a = ["2020-03-01", "2022-05-06", "2022-07-06"]  # 비가 온 날
b = ["2020-03-01", "2022-05-09"]    # 우산을 가지고 간 날          
print(solution(a, b))