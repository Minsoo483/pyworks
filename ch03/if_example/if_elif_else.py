age = int(input("나이 입력 :"))
charge = 0

if age <= 8:
    print("취학 전 아동입니다.")
    charge = 1000
    
elif age <14:
    print("초등학생입니다.")
    charge = 2000

elif age <= 20:
    print("중,고등학생 입니다.")
    charge =2500

else:
    print("일반인 입니다.")
    charge = 3000


print("입장료는 %d원입니다." %charge)
