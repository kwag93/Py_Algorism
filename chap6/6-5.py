# 계수정렬
# 이는 가장 큰 데이터와 작은 데이터의 차이가 100만을 넘지 않을때 효과적이다
# 또한 양의 정수인 경우여야 한다
# 이때 최악의 경우여도 N + K 의 시간복잡도를 보장해준다.
arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

cnt = [0] * (max(arr) + 1)

for i in range(len(arr)):
    cnt[arr[i]] += 1
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=' ')
