# Day_03_01_list.py

# collection : list[], tuple(), set{}, dictionary{}
# list is most important among them (about 80% of all)

a = [1, 4, 7]
print(a)
print(len(a))
print(a[0], a[1], a[2])

# Quiz : sum of list a
print(a[0] + a[1] + a[2])

# Quiz : 반복문을 사용해서 리스트 a의 합계를 구하세요.
total = 0
for i in range(len(a)):
    total += a[i]
print(f'Answer : {total}')
print(sum(a))   # sum 이런건 잘 안씀 : 약간 초딩 수준?
print('-' * 30)

print(a)
a[0] = 3
print(a)

# Quiz : 리스트 a를 거꾸로 출력하세요
for i in range(len(a)-1, -1, -1):   # bad code
    print(a[i], end=' ')
print()

for i in reversed(range(len(a))):   # good code
    print(a[i], end=' ')
print()
print('-' * 30)

# Quiz : 리스트 a 에 들어있는 홀수의 갯수를 구하세요.
cnt = 0
for i in range(len(a)):
    if a[i] % 2:
        cnt += 1
    # else:
    #     cnt += 0
print(f'홀수 갯수 : {cnt} 개')

# 1 대신 쓸 수 있는 것?
cnt = 0
for i in range(len(a)):
    cnt += a[i] % 2
print(f'홀수 갯수 : {cnt} 개')
print('-' * 30)

for i in a:
    print(i)