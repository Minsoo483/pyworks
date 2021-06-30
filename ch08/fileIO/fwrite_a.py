#a는 추가로 쓰기 -> w로 쓰면 초기화 됨
f = open('C:/pyfile/hello.txt', 'a')
f.write('dog\n')
f.write('cat\n')
f.close()