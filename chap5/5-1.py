# stack 기초

stack = []
# python에는 이를 지원하는 라이브러리가 따로없음
# 리스트가 스택과 같이 작동
# append 와 pop 을 사용해보자
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.pop()

print(stack) 
# 5 2 
print(stack[::-1])
# 2 5 최상단부터 출력해줌
