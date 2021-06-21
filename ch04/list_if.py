
print("for in 구문")
score = [70,80,50,60,90,45]
index = 0

for i in score:    # i는 리스트의 값을 의미
    index += 1
    if i >= 60:
        print("%d번 학생은 합격입니다." %index)
    else :
        print("%d번 학생은 불합격입니다." %index)

print('=' * 50)

print("for in range() 구문")

for i in range(0,len(score)):  # i는 인덱스
    
    if score[i] >= 60:
        print("%d번 학생은 합격입니다." %(i+1) )
    else :
        print("%d번 학생은 불합격입니다." %(i+1))
