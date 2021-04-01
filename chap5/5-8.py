# DFS 예제
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # 다른 노드 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 방문정보 노드만큼 
visited = [False] * 9

dfs(graph, 1, visited)