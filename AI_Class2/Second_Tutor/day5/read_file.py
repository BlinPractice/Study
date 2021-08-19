# readline : 한 줄 씩 읽기
# f = open("new.txt", "r", encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close() # 파일이 close 나올 때 까지 계속 열려있음

# readlines : 여러 줄 읽기
# f = open("new.txt", "r", encoding="utf-8")
# lines = f.readlines()
# f.close()   # lines에 내용을 담아놓고 파일 닫음 (효율적)
# for line in lines:
#     print(line)

# read : 전체 다 읽기
f = open("new.txt", "r", encoding="utf-8")
text = f.read()
f.close()
print(text)