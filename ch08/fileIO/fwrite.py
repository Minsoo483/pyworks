# 파일 열기 open -> 파일 쓰기 write -> 파일 닫기 close
f = open('C:/pyfile/hello.txt', 'w')
f.write("Hello~ python\n")
# f.write(100) -> 숫자는 입력불가 - format 방식으로 입력

f.write("%.1f\n" % 7.3)
num = "%d\n" % 100000
f.write(num)
f.write("안녕! 파이썬")
f.close()
