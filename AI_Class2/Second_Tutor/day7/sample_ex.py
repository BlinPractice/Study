import csv
import matplotlib.pyplot as plt
import datetime as dt

data = []
with open('C:/Users/user/OneDrive/바탕 화면/ws/day6/sample.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for text in reader:
        data.append(text)

down_30_am = 0
down_30_pm = 0
up_30_am = 0
up_30_pm = 0
for datum in data:
    datum_dt = dt.datetime.strptime(datum[2], '%Y-%m-%d %H:%M:%S')
    if int(datum[3]) < 30:
        if datum_dt.hour < 12:
            down_30_am += +1
        else:
            down_30_pm += 1
    else:
        if datum_dt.hour < 12:
            up_30_am += +1
        else:
            up_30_pm += 1

plt.figure(figsize=(8,8))
x = [0,1]
y1 = [down_30_am, up_30_am]
y2 = [down_30_pm, up_30_pm]

plt.bar(x, y1, color='r', label='am')
plt.bar(x, y2, bottom=y1, color='b', label='pm')
plt.title('example')
plt.xlabel('age')
plt.ylabel('number')
plt.xticks(x, ['30>', '30<='])
plt.legend()
plt.show()