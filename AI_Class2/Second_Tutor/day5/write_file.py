f = open("new.txt", "a", encoding="utf-8")

for i in range(10):
    sentence = f"{i+11}번째 줄 입니다.\n"
    f.write(sentence)

f.close()

# 'r':read, 'w':write, 'a':append
