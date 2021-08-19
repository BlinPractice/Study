import csv

# with open('c:/Users/user/OneDrive/바탕 화면/ws/day6/sample.csv') as f:
#     csv_data=[]
#     for line in f.readlines():
#         csv_data.append(line.split(','))
# print(csv_data)


with open('c:/Users/user/OneDrive/바탕 화면/ws/day6/sample.csv') as f:
    reader = csv.reader(f)

    print(reader)
    print(type(reader))

    for text in reader:
        print(text)
