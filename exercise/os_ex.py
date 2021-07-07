import os

'''
os.chdir("c:/")
dir = os.popen("dir")
print(dir)
print(dir.read())'''

# 디렉터리 이름 - list로 반환
dirnames = os.listdir("c:/pyworks/exercise")
print(dirnames)
print(dirnames[0])
print(dirnames[-1])

for dirnames in dirnames:
    print(dirnames)
