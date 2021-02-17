# n, m, k 를 공백으로 구분해서 입력받기

n, m, k = map(int, input().split())
data = list(map(int, input(), input()))

data.sort() #리버스 하지 않아서 내림차순임
one = data[n - 1]  #가장큰수 
two = data[n - 2] #두번째로 큰 수 

result = 0

while 1:
  for i in range(k):
    if m == 0:
      break
    result += one
    m -= 1
  if m == 0:
    break
  result += two
  m -= 1

print(result)
'''
의사코드
받은 값을 sort
6 5 4 4 2
m 만큼 더하고 k번만 가능
m 값만큼 for문 반복하기
6 k번 5 k번 4k번 (이때 인덱스 0 1 2 순서로)
최종 sum 값을 도출한다
'''

'''
내가 부족했던 부분 
1. map 과 split을 통한 공백으로 나누어 입력받기가 익숙치 않음
이는 input 을 이용하면 문자열로 받아지는 값을 split을 통해 공백을 나누고 int로 변환하는 과정을 거치는 부분이다.
2. 만약 범위가 더 크다면 문제가 생길 수 있음 (m이 100억이라면?)
이를 해결하기 위해 특정 수열을 만들어주면 더 손쉽게 해결이 가능
이는 문제를 풀때 항상 예시를 통해 적어보며 어떤 수열이 반복되는지를 체크해보아야 한다.
int(M / (K + 1) * K + M % (K + 1 ))이라는 수열을 도출 가능하다.

cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)

result = 0
result += (cnt) * one 
result += (m - cnt) * two 
'''