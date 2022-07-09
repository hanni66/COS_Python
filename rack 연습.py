# 순위 구하기 1
scores = [20, 394, 342, 32, 90]

ranking = [1]*len(scores)

for i in range(len(scores)):
    for j in range(len(scores)):
        if scores[i] < scores[j]:
            ranking[i] += 1

print(ranking)

# 순위 구하기 2
scores = [20, 394, 342, 32, 90]

ranking = []

for i in range(len(scores)):
    rank = 1
    for j in range(len(scores)):
        if scores[i] < scores[j]:
            rank += 1
    ranking.append(rank)
    
print(ranking)

# 순위 구하기 3
scores = [20, 394, 342, 32, 90]

ranking = []

for i in scores:
    rank = 1
    for j in scores:
        if i < j:
            rank += 1
    ranking.append(rank)
    
print(ranking)

# 순위 구하기 4
scores = [20, 394, 342, 32, 90]

scores.sort(reverse=True)
print(scores)

for i in range(len(scores)):
    if scores[i] == 90:
        print(i+1)

# eumerate로 바꾸기 
# 순위 구하기 5
scores = [20, 394, 342, 32, 90]

scores.sort(reverse=True)

for i,v in enumerate(scores):
    if v == 90:
        print(i+1)