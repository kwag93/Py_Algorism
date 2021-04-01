n, m = map(int, input().split())

#map 생성하여 0으로 초기화하기
d = [[0] * m for _ in range(n)]
# x y 방향좌표받기
x,y ,dic = map(int, input().split())
  # 현재 좌표 처리
d[x][y] = 1

# 전체맵
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 방향정의
# 북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 회전
def turn_left():
    global dic
    dic -= 1
    if dic == -1:
        dic = 3

cnt = 1
turn_time = 0
while 1:
    turn_left()
    nx = x + dx[dic]
    ny = y + dy[dic]
    # 왼쪽 회전했는데 가보지 않은 칸이 존재하면
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    # 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 모든 방향을 가지 못하는 경우
    if turn_time == 4:
        nx = x - dx[dic]
        ny = y - dy[dic]
        #뒤로가기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        #바다
        else:
            break
        trun_time = 0
print(cnt)

# 의사코드
# 맵을 받아 그만큼의 이차원 배열을 생성한다
# 캐릭터의 x,y 좌표를 저장하고 해당 위치에서 움직일때마다 동 서 남 북에 따라 이동한다.
# 이동할때마다 cnt 값을 늘려준다
