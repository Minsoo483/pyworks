
def divide(x, y):
    try:
        div = x / y
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else:
        print(div)
    finally:
        print("반드시 출력")


divide(3,0)
