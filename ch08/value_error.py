while True:
    try:
        x = int(input('숫자를 입력하세요 : '))
        print(x)
        break
    except ValueError:
        # print(e)
        print("유효한 숫자가 아닙니다. 숫자를 입력해주세요.")


