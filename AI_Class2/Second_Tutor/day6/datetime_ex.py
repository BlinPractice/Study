import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, '')

# 1. 2021년 8월 11일과 1994년 1월 27일의 차이 일자는?
print('문제 1 : ', end='')
day1 = dt.date(2021,8,11)
day2 = dt.date(1994,1,27)
print(day1 - day2)

# 2. 자신의 생일을 "xxxx년 xx월 xx일 x요일"로 출력.
print('문제 2 : ', end='')
my_birth = dt.date(1996,3,6)
weekday = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
birth_day = my_birth.strftime("%Y년 %m월 %d일 ")
birth_date = weekday[my_birth.weekday()]
print(birth_day + birth_date)

# 3. 다음 생일까지 남은 시간은?
print('문제 3 : ', end="")
print(dt.datetime(2022,3,6) - dt.datetime.now())