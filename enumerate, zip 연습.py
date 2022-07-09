# eumerate 함수 

x = ['a', 'b', 'c']

# 인덱스 번호와 데이터 값을 쌍으로 나타냄.
e = list(enumerate(x))

print(e)

# 자주 나오는 문장이다.
for i, v in enumerate(x):
    print(i, v)


# zip 함수 

kor = [10, 20, 30]
eng = [40, 50, 60]

for k, e in zip(kor, eng):
    print(k, e)

