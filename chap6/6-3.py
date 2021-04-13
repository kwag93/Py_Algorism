# 퀵 정렬
# 이는 일반적인 형태이다
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end: # 원소가 하나이면 종료한다
        return
    pivot = start
    left = start + 1
    right = end 
    while left <= right:
        # 피벗보다 큰 수를 찾자
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾자
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: #엇갈린경우
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)