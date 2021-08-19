import datetime as dt

dt1 = dt.datetime(1994, 1, 27, 3)
dt2 = dt.datetime(2012, 7, 12, 20)
print(dt1)
print(dt2)

# timedelta
td1 = dt2-dt1
print(td1)

print(type(dt1))
print(type(td1))

print(dt1 + td1) # = dt2 