# 삽입 정렬 
# 거의 정렬이 되어있는 자료를 정렬시 효과적

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1): # i부터 1까지 감소하며 반복된다
        if arr[j] < arr[j - 1]: #한 칸씩 왼쪽으로 이동
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break
print(arr)