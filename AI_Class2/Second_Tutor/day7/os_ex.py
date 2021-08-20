import os

# C:\Users\user\OneDrive\바탕 화면\ws
cpath = os.getcwd()
print(cpath)
print(os.listdir())

# C:\Users\user\OneDrive\바탕 화면\ws\day7
os.chdir('day7')
cpath = os.getcwd()
print(cpath)
print(os.listdir())

# C:\Users\user\OneDrive\바탕 화면\ws
os.chdir('../')
cpath = os.getcwd()
print(cpath)

# 폴더 만들기
dir_name = 'day8'
if 'day8' not in os.listdir():
    os.mkdir('day8')
    print(f"{dir_name} 폴더를 만들었습니다.")
else:
    print(f"현재 경로 ({os.getcwd()})에 이미 {dir_name}이 존재합니다.")

# 파일 만들기
os.chdir(dir_name)
with open('test.txt', 'w', encoding='utf-8') as f:
    for i in range(10):
        sentence = f"{i+1}번째 줄 입니다.\n"
        f.write(sentence)
