# Day_03_02_slicing.py

a = list(range(10))
print(a)

print(a[0:3])

# Quiz : 리스트 a 의 앞쪽 절반을 출력하세요.
print(a[:len(a)//2])

# Quiz : 앞쪽 절반, 뒷쪽 절반을 출력하세요.
half = len(a)//2
print(f'앞쪽 절반 : {a[:half]}')
print(f'뒷쪽 절반 : {a[half:]}')
print()

# Quiz : 리스트 a 에서 짝수번 째만 출력, 홀수번 째만 출력하세요
print(f'짝수번 째만 출력 : {a[::2]}')
print(f'홀수번 째만 출력 : {a[1::2]}')
print()

# Quiz : 리스트 a 를 슬라이싱하여 거꾸로 출력하세요
print(a[::-1])
print()

# 증감(양수) : 왼쪽에서 오른쪽으로 진행
print(a[::1])
# 증감(음수) : 오른쪽에서 왼쪽으로 진행
print(a[::-1])

# Quiz : 리스트 a 를 짝수번 째만 거꾸로, 홀수번 째만 거꾸로 출력하세요
print(f'짝수 거꾸로 : {a[-2::-2]}')
print(f'홀수 거꾸로 : {a[::-2]}')
