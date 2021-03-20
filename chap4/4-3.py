input_data = input() 
x = int(input_data[1])
y = int(ord(input_data[0]))-int(ord('a')) + 1

steps = [(2,1) , (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

cnt = 0

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if next_x >= 1 and next_x <= 8 and next_y >= 1 and  next_y <=8:
        cnt += 1
print(cnt)


#의사코드
# 좌표로 이루어진 문자를 받아 두개를 나누어 각각 저장하자. 행과열이기 때문
# 경우의 수를 체크하기 위해 해당 조건을 만들어주고 확인한다. 모든 경우를 작성
# 맵에서 벗어나지 않는지를 확인해주어야 함


# 아쉬운점
# y값을 변환해야한다는걸 생각못함. Int로 단순변환하려고 했는데 생각해보니 python에는 Ord함수가 존재해서 그걸 사용하면 더 쉽게 변환이 가능했음
