# 성적이 낮은 순서로 학생을 출력하라

n = int(input())

def down(key):
    return key[1]
arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))
arr = sorted(arr, key=down)

for i in arr:
    print(i[0], end=' ')





# 두개의 값을 받는 방법 data  0 1 
# def 를 사용하는 방법 그리고 람다를 사용하는 방법
# 결국 이는 원하는 배열의 인자를 키로 사용하기 위함임