n = int(input())

cnt = 0
for i in range(n + 1):
    for second in range(60):
        for minite in range(60):
            if '3' in str(i) + str(second) + str(minite):
                cnt += 1
print(cnt)

# 의사코드 : 3이라는 숫자를 찾는건 제시되었기 때문에 이를 시 분 초를 반복하여 해당 문자열에 존재하면 +1 을 해준다
