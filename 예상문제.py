# 1부터 10까지의 합
answer = 0
for i in range(1,11):
    answer += i
print(answer)

# 10부터 1까지의 합
answer = 0
for i in range(10,0, -1):
    answer += i
print(answer)

# n!
n = 5
re = 1
for i in range(n, 0, -1):
    re *= i
print(re)

# 소문자의 개수
a = "Test01Yes"
count = 0

for i in a:
    if i.islower() == True:
        count += 1
print(count)

c = 0
for s in a:
    if s >= 'a' and s <= 'z':
        c += 1
print(c)        