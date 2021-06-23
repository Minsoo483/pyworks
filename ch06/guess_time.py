# 20초 세어 맞히는 프로그램

import time
import math

input('Enter를 누르고 20초를 셉니다')
start = time.time()

input('20초 후에 다시 Enter를 누르세요')
end = time.time()

et = end - start
print('실제 시간 : ', et , '초')
print('시간 차이 : ', abs(20 - et) ,'초')

