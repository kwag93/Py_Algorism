n = 1260
cnt = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types: #파이썬에서 가능한 특이한 for in문
  cnt += n // coin 
  n %= coin 
print(cnt)

#동전을 이용한 간단한 그리디 알고리즘 구현