# Day_04_01_numpy.py

import numpy as np

a = np.arange(10)
print(a)
print(len(a))
print(type(a))
print(a.dtype, a.shape)

# Quiz : 넘파이 배열을 거꾸로 출력하세요.
print(a[::-1])
print('-' * 30)

# very important in numpy
print(a + 1)    # broadcast : 모든 항에 대해 스칼라 값을 전파하는 느낌
print(a + a)    # vector (array) : 배열과 배열의 계산 (같은 위치만 해당)
print('-' * 30)

# dimension change
print(a.reshape(2, 5))
print(a.reshape(2, 5).shape)
print()
print(a.reshape(5, 2))
print(a.reshape(5, 2).shape)
print('-' * 30)

# Quiz : 1차원 배열 b를 2차원 배열로 변환하세요. (모든 가능한 방법 적용)
b = np.arange(12)
print(f'original b : \n{b}\n')
print(f'1 x 12 : \n{b.reshape(1, 12)}\n')
print(f'2 x 6 : \n{b.reshape(2, 6)}\n')
print(f'3 x 4 : \n{b.reshape(3, 4)}\n')
print(f'4 x 3 : \n{b.reshape(4, 3)}\n')
print(f'6 x 2 : \n{b.reshape(6, 2)}\n')
print(f'12 x 1 : \n{b.reshape(12, 1)}\n')

print(f'np.reshape : \n{np.reshape(b, [2, 6])}\n')
print(f'뒤에 생략 가능 : \n{np.reshape(b, [2, -1])}\n')
print(f'앞에 생략 가능 : \n{np.reshape(b, [-1, 6])}')
print('-' * 30)

# broadcast and vector operation
c = b.reshape(2, 6)
print(f'original c : \n{c}\n')
print(f'broadcast : \n{c + 1}')
print(f'vector : \n{c + c}')

# Quiz : 2차원 배열 c에서 첫 번째와 마지막의 요소를 출력하세요.
print(f"\nfirst : {c[0][0]} {c[0, 0]}")
print(f"last : {c[-1][-1]} {c[-1, -1]}")    # fancy indexing
print('-' * 30)

# Quiz 1 : 2차원 배열 d에서 마지막 행을 제외한 전체를 출력하세요.
# Quiz 2 : 2차원 배열 d에서 마지막 열을 제외한 전체를 출력하세요.
d = b.reshape(3, 4)
print(f'original d : \n{d}\n')
print(f'Quiz 1 : \n{d[:-1]}\n')
print(f'Quiz 2 : \n{d[:, :-1]}')
