# 몇개를 입력받을 것인지

n = int(input())

# n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력

for i in array:
    print(i, end=' ')