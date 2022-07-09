# 공배수 찾기
a = 4
b = 6

answer = 0

for i in range(1, a*b+1):
    if i%a == 0 and i%b == 0 :
        print(i)

print('==============')

# 최소 공배수 찾기 - 1
a = 4
b = 6

answer = 0

for i in range(1, a*b+1):
    if i%a == 0 and i%b == 0 :
        print(i)
        break   # 찾자마자 바로 break를 하니 최소 공배수를 찾을 수 있다.

print('==============')

# 최소 공배수 찾기 - 2
a = 4
b = 6

for i in range(1,b+1):
    if (a*i) % b == 0:
        print(a*i)
        break

print('==============')

# 공약수 구하기 
a = 4
b = 6

for i in range(1, min(a, b)+1):
    if a%i == 0 and b%i == 0 :
        print(i)

print('==============')
# 최대 공약수 구하기
a = 4
b = 6

for i in range(min(a, b)+1, 1, -1):     #  최소 값부터 1까지 거꾸로 반복하기 
    if a%i == 0 and b%i == 0 :
        print(i)
        break
