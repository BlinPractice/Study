# 사용자 모듈

# 모듈명 : my_lib.py


# 함수명 : my_max()
# 인수 : 최대값을 구하고자 하는 값을 저장한 list
# 반환값 : 최대값
def my_max(l):
    max_value = None

    if len(l) > 0:
        max_value = l[0]
        print(l)
        for v in l:
            print(v)
            if v > max_value:
                max_value = v

    return max_value


# 함수명 : my_min()
# 인수 : 최소값을 구하고자 하는 값을 저장한 list
# 반환값 : 최소값
def my_min(l):
    min_value = None

    if len(l) > 0:
        min_value = l[0]
        print(l)
        for v in l:
            print(v)
            if v < min_value:
                min_value = v

    return min_value
