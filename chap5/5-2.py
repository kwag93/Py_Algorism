from collections import deque 
# que를 사용해보기 위한 라이브러리
# deque 의 경우 스택과 큐 모든 장점을 사용한다
queue = deque()

queue.append(5) 
queue.append(1)
queue.append(3)
queue.popleft() 
queue.append(4) 
queue.popleft() 

print(queue)
# 3 4 
queue.reverse() 
# 4 3 
print(queue)
# 4 3 
print(list(queue))
# list 객체로 반환한것이다
