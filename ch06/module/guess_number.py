#숫자 추측 게임

import random as r

com = r.randint(1, 30)
while True:
    try:
        guess = int(input('맞혀보세요(1~30): '))
        if guess > 30 or guess < 1:
            print("범위를 초과했어요. 다시 입력해주세요")
        elif com > guess:
            print('너무 작아요!!')
        elif com < guess:
            print('너무 커요!')
        else:
            print('정답')
            break
    except ValueError:
        print("숫자가 아닙니다. 다시 입력해 주세요: ")
