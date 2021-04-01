# 재귀함수의 대표적인 예시인 팩토리얼 예시
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))