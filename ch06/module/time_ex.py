import time

print(time.time()) #1970년 1월 1일 자정이 기준 -> 1624409726.5322342

print(time.localtime()) #time.struct_time(tm_year=2021, tm_mon=6, tm_mday=23,
                        #tm_hour=9, tm_min=55, tm_sec=26, tm_wday=2, tm_yday=174, tm_isdst=0)

print(time.ctime()) # Wed Jun 23 09:55:26 2021

print(time.strftime('%x', time.localtime())) # 06/23/21

print(time.strftime('%c', time.localtime())) #Wed Jun 23 09:57:10 2021

# time.sleep(1) : 1초간 대기 python은 1초 -> 1로 표기
for i in range(1, 11):
    print(i)
    time.sleep(0.1)
