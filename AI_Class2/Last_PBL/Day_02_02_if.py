# Day_02_02_if.py

# odd and even, night and day, light and darkness, male and female, cold and hot

# Quiz : 어떤 양수에 대해 홀수인지 짝수인지 알고 싶습니다.
a = 72
# bad code
if (a % 2) == 1:    # 1 == 1 이런 꼴... 똑같은 말을 반복하는 나쁜 코드
    print(f'{a} is 홀수')
else:
    print(f'{a} is 짝수')

# good code
if a % 2:
    print(f'{a} is 홀수')
else:
    print(f'{a} is 짝수')

a = 0
if a:
    print(f'{a} is 홀수')
else:
    print(f'{a} is 짝수')
print('-' * 30)
##################################################################

# Quiz : 어떤 정수가 음수인지, 0인지, 양수인지 알려주세요.
b = 3
# bad code : 모든 코드 실행 --> CPU 혹사
if b < 0:
    print(f'{b} is 음수')
if b > 0:
    print(f'{b} is 양수')
if b == 0:
    print(f'{b} is zero')
print('end 1')

# good code : 해당 코드만 실행 --> CPU 효율적
if b < 0:
    print(f'{b} is 음수')
elif b > 0:
    print(f'{b} is 양수')
else:
    print(f'{b} is zero')
print('end 2')
print('-' * 30)
##################################################################

# Quiz : 1000보다 작은 양수의 자릿수를 알려주세요 (1 ~ 999)
c = 123
if c < 10:
    print(1)
elif c < 100:
    print(2)
else:
    print(3)

if c >= 100:
    print(3)
elif c >= 10:
    print(2)
else:
    print(1)