# 인접 리스트 방식 예제
# 리스트 자료형을 이용하여 연결리스트 처럼 구현한다

graph = [[] for _ in range(3)]

# 노드 0 에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 저장
graph[1].append((0, 7))

#노드 2에 저장
graph[2].append((0,5))

print(graph)