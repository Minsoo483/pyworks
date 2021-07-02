
with open('scorelist.txt', 'r') as f:
    d2 = []
    for i in range(3):
        d2.append(f.readline().split())

    for i in range(3):
        d2[i][1] = int(d2[i][1]) # 국어점수 계산을 위해 int로 변환
        d2[i][2] = int(d2[i][2])

        sum = d2[i][1] + d2[i][2]
        d2[i].append(sum)

        avg = sum / 2
        d2[i].append(avg)

    print('   *********** 성적표 ***********  ')
    print('   =============================   ')
    print("   이름    국어  수학  총점  평균 ")
    print('   =============================   ')
    for i in range(3):
        print('   {}   {}   {}   {}  {}'.format(d2[i][0], d2[i][1], d2[i][2], d2[i][3], d2[i][4]))
    print('   =============================   ')
    print("   ********  과목별 평균 *********   ")
    kor_sum = 0
    math_sum = 0
    for i in range(3):
        kor_sum += d2[i][1]
        math_sum += d2[i][2]
    print("   국어 : %.1f,  수학 : %.1f" % (kor_sum/3, math_sum/3))

