
dan = int(input("단을 입력하세요."))

for i in range(1,10):
    print("%d x %d = %d" %(dan,i, dan*i))

#구구단 전체
for i in range(2,10):
    for j in range(1,10):
        print("%d x %d = %d" %(i,j, i*j))

