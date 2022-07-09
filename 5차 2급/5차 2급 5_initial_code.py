# 공약수를 찾는다 -> 둘 중의 작은 수까지만 반복해야 됨.
# 공배수를 찾는다 -> 두 수를 곱한 것까지만 찾는다.
def solution(a, b):
    answer = 0
    for i in range(1, b + 1):
        if (a * i) % b == 0:
            answer = a * i
            break
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
a = 4
b = 6
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")