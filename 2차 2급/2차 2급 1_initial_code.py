max_product_number = 10

# func_a 는 엄청 많이 나온다 !!!!!!!! 다시 풀어보기
def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
        counter[x] += 1
    return counter

# def func_a(gloves):
#     counter = [0]*(max_product_number+1)
#     for x in gloves:
#         counter[x] += 1
#     return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    # zip으로 바꿔보기 
    # for x,y in zip(left_counter, right_counter):
    #     total += min(x, y)
    return total


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")