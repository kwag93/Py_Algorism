n, k = map(int, input().split())
result = 0

while 1:
    target = (n // k) * k #딱 떨어지게 
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)
'''
의사코드:
값을 n과 k 를 %를 통해 나누어주고
그 나머지만큼 -1 을 수행한다음
수행된 값을 / 처리하면 가장 최소의 단위가 될것이다.
필요한것 cnt mok 
'''

'''
while (n > 1):
    if(n % k != 0):
        re = n % k 
        for i in range(re):
            n -= 1
            cnt += 1
    else:
        n /= k
        cnt += 1
print(cnt)
다른 테스트 케이스를 더 찾지 못함 다만 뺀 값을 그대로 cnt에 더하는게 더 효율적
어차피 그 케이스를 더 실행할 필요가없다.
'''