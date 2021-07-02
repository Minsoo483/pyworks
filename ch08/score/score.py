while True:

    ans = input("성적을 저장할까요?(y/n)")
    if ans == 'y' or ans == 'Y':
        with open('scorelist.txt', 'a') as f:
            name = input("이름 입력 :")
            f.write(name + ' ')
            try:
                kor = int(input("국어점수 입력 :"))
                f.write(str(kor) + ' ')

                math = int(input("수학점수 입력 :"))
                f.write(str(math) + '\n')

                # avg = (kor + math) / 2
                # f.write(str(avg) + '\n')
            except ValueError:
                print("숫자를 입력해주세요")

    elif ans == 'n' or ans == 'N':
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요")


with open('scorelist.txt', 'r') as f:
    data = f.read()
    print(data)