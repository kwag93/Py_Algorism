# 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

a.sort() 
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    if a[i] == b[i]:
        continue
print(sum(a))

# if 문에서 같은경우 컨티뉴 말고 그냥 같거나 크면 바로 반복문을 종료해도 괜찮다 (정렬된 상태이기 때문에)