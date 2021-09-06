# Day_02_01_PythonBasic.py

print(12, 3.14, True, 'Hello')
print(type(12), type(3.14), type(False), type("Hello"))
print(type('12'))

# 사칙연산(산술연산)
# print(12 + '12') --> Error
print(12 + 3.14)

# programming (programme : 편성표)
# 구성요소 : code(function), data(변수, 상수)
# 함수와 변수의 구분 : () 있으면 함수, 없으면 변수
a, b, a = 3, 5, 99
print(3, a)
print()     # 빈 줄 추가
# text code --> binary file --> OS 실행

##################################################################

a, b = 3, 5
print(a, b)     # 3 5

# Quiz : a와 b의 값을 교환하세요
a, b = b, a
print(a, b)     # 5 3

##################################################################

# 연산 : 산술, 관계, 논리
# 산술연산 : +, -, *, /, **, //, %
a, b = 7, 3
print(a + b)
print(a - b)
print(a * b)
print(a / b, '\n')
print(a ** b)   # 지수 : a ^ b
print(a // b)   # 몫 (정수 나눗셈)
print(a % b, '\n')    # 나머지

#     2
#   +---
# 3 | 7
#     6
#    ---
#     1

s, t = 'sky', 'blue'
print(s + t)
print(s * 3)
print('-' * 30)

# Quiz : 두 자리 양수를 갖고 있는 변수 a의 값을 거꾸로 바꿔주세요
a = 27
print(f'original a : {a}')
b = a // 10
c = a % 10
a = c*10 + b
print(f'changed a : {a}')
print('-' * 30)

# 관계연산 : >, >=, <, <=, ==, !=
a, b = 7, 3
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b, '\n')
print('ace' > 'bed')    # ASCII code value
print(ord('a') + ord('c') + ord('e'))
print(ord('b') + ord('e') + ord('d'))
print('-' * 30)

# 논리연산 : and, or, not
print(True and True)
print(True and False)
print(False and True)
print(False and False)
