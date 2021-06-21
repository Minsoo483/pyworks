size = int(input("한 변의 길이를 입력하세요 :"))
area = size * size
#print("정사각형의 넓이 : ",area,"cm^2")
print("정사각형의 넓이 : %dcm^2" % area )
''' <대응 문자>
%d -> 정수
%f -> 실수 %.2f는 소수점 둘째자리까지만 표시.
%s -> 문자
'''

width = int(input("밑변의 길이를 입력하세요 :"))
height = int(input("높이를 입력하세요 :"))
area = (width * height) / 2
print("삼각형의 넓이 : %dcm^2" %area)
