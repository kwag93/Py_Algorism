# 선택 정렬

arr = [7, 6, 9, 0, 2, 1, 4, 8]

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # arr swap 함수
print(arr)

# 시간복잡도가 N^2 이기 때문에 1만개 이상의 데이터를 정렬하면 급격히 느려지는 단점이 있다.
