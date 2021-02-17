n = int(input())
x, y = 1, 1
plans = input().split()

dx = (0, 0, -1, 1) #x값의 변화
dy = (-1, 1, 0, 0)
move = ['L', 'R', 'U', 'D']

#계획들 앞에서부터 체크
for plan in plans:
    #계획에 따른 이동후의 좌표 
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어날경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #실제 이동실행
    x, y = nx, ny
print(x, y)
'''
의사코드:
기본적으로 1~n까지의 값이 들어가는 n * n 2차원 배열을작성한다.
최초의 값을 (1,1)로 놓고 if문을 통해 해당 명령어가 가능한지 체크하고 진행, 체크하고 진행 방식으로 진행해보자

부족했던점:
애초에 2차원 배열을 작성해서 할 필요가 없었음. 좌표값을 그려야 한다고 생각한것부터가 실수
심지어 인풋값을 split을 통해 받으면 자동으로 [a, b, c]로 들어간다. 파이썬에 익숙하지 않아 생기는 오류
또한 n 값을 int로 받지 않아 값이 비교되지 않는 부분이 있었음.
'''


