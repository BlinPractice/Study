# Day_02_03_for.py

# 0 1 2 3 4     0, 4, 1
# 0 2 4 6 8     0, 8, 2
# 4 3 2 1 0     4, 0, -1

for i in range(5):
    print(i, end=' ')
print()

for j in range(0, 10, 2):   # 9 대신 10을 써야 규칙에 알맞음
    print(j, end=' ')
print()

for k in range(4, -1, -1):
    print(k, end=' ')
print()
print('-' * 30)

# 변형 : Hello 반복 출력
for i in range(0, 5, 1):
    print('Hello' * i)
print()

# Quiz : 1부터 100까지 정수 합계를 구하시오.
total = 0
for i in range(1, 101):
    total += i
print(f'1 ~ 100 : {total}')
print(sum(range(1, 101)))
print()

# 모두 똑같은 코드 : 0 1 2 3 4
for i in range(0, 5, 1):
    print(i, end=' ')
print()

for i in range(0, 5):
    print(i, end=' ')
print()

for i in range(5):
    print(i, end=' ')
print()
