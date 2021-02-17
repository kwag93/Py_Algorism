n, m = map(int,input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_num = 10001
  for j in data:
    min_num = min(min_num, j)
  result = max(result, min_num)
print(result)

#(풀이2)

n, m = map(int, input().split())
result = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_num = min(data)
  result = max(result, min_num)
print(result)
'''
의사코드:
각 행마다 작은 숫자를 찾아서 그 수중에 가장 큰수를 찾아내자
이중 반복문을 통해 while 로 행 그다음 수 방식으로 가장 작은 숫자를 찾고
이를 저장해 그 리스트에서 가장 큰 수를 뽑아내면 될것이다.
'''

'''
내가부족했던 부분:
파이썬에서의 이중 for문은 range를 통해 사용가능
data를 리스트로 받아 사용가능하다. 
c처럼 생각해서 배열을 리스트처럼 사용하려고 했는데 그럴필요없었음
data 부분에서 자동으로 [ 3 1 2 ] 를 생성한다
range(n) 또한 0 1 2 까지 진행을 시켜줌 
j 에는 3 1 2 가 순서대로 들어가게 됌
파이썬의 for문에 익숙하지 않았던것이 문
'''