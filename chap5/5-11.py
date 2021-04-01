from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어남
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인경우
            if graph[nx][ny] == 0:
                continue
            #처음 방문
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지
    return graph[n - 1][m - 1]

print(bfs(0, 0))

# 이해가 잘 안됌 다시 살펴볼것