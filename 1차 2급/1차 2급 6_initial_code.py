
# 숫자 추출
# n = 135

# while n> 0 :
#     last = n%10
#     n = n//10

#     print(last, n)

#숫자 추출

# n = 135642349

# while n > 0 :
#     last = n%10
#     if last ==3 or last ==6 or last==9:
#         print("박수")
#     else:
#         print(last)
#     n = n//10

#     print(last, n)


def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

#The following is code to output testcase.
number = 40
ret = solution(number)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
