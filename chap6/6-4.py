# 파이썬 개선 퀵정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return
    
    pivot = arr[0]
    tail = arr[1:] # 피벗을 제외한 나머지

    left_side = [x for x in tail if x <= pivot] #왼쪽
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 각각 정렬 후 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))

# nlogn 의 빠른 속도를 지녔다. 단 무작위 데이터가 들어오는 최악의 경우 n^2 이다
# 데이터가 정렬되어 있다면 느리다.
# 다만 기본 정렬 라이브러리를 사용하면 nlogn 을 보장해준다
