import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, '')

now = dt.datetime.now()
print(now)

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)

# weekday
weekday = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
print(weekday[now.weekday()])

# strftime
print(now.strftime("%b월 %d일 %A"))

# date
print(now.date())

# time
print(now.time())

day1 = dt.datetime(2021, 10, 5, 19)
day2 = dt.date(2020, 12, 10)
print(day1)
print(day2)
