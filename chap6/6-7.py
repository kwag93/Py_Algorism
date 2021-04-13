# 위에서 아래로
# 입력된 수를 큰수부터 작은수로 출력하라

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)
for i in arr:
    print(i, end= ' ')