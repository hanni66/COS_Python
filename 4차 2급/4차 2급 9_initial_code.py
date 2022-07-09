#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(height):
    #여기에 코드를 작성해주세요.
    count = 0
    # 규칙 정의 암기하기 
    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    for i in range(4):
        for j in range(4):
            # print("기준 좌표점: ", i, j, "값: ", height[i][j])
            is_danger = True
            for k in range(4):      # 상하좌우를 돌면서 자기 값보다 작은 값이 있는 지 확인하는 반복문 
                if 0 <= i+di[k] < 4 and 0 <= j+dj[k] < 4 :
                    if height[i+di[k]][j+dj[k]] < height[i][j]:
                        is_danger = False
            if is_danger == True:
                count += 1
                print(i, j, height[i][j])
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")