def avg(a):
    sum = 0
    for i in a:
        sum += i
    result = sum/len(a)
    return result

avg = avg([70,80,60,90,100])
print("평균 점수 : {}".format(avg))
print("평균 점수 : %.f" %avg)
