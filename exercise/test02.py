#1번
ko =80
en= 75
ma = 55


sum = ko+en+ma

avg = sum / 3

print("세 과목의 평균 : ",avg)

#2번
num=13
if num % 2 ==0 :
    print("짝수")
else:
    print("홀수")

#3번,4번
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print("연월일 : ",yyyymmdd)
print("숫자 : ",num)

gender = pin[7]
if gender == "1":
    print("남자입니다.")
else :
    print("여자입니다.")

#5번

a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#6번

a = [1,3,5,4,2]
a.sort()
a.sort(reverse=1)
print(a)

#7번

a = ['Life','is','too','short']
result = " ".join(a)
print(result)

#split() 예제
s = "Life is too short"
s = s.split()
print(s)

s = "a:b:c:d"
s = s.split(":")
print(s)

#8번
a= (1,2,3)
a= a +(4,)
print(a)

#9번
a = dict()
a['name']='python'
a[('a',)]='python'
# a[[1]]='python' -> 리스트라 오류
a[250]='python'

#10번
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11번
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#12번
a = b = [1,2,3]
a[1] = 4
print(b)
