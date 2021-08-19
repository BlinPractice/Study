with open("new.txt", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    if not line: break
    print(line)