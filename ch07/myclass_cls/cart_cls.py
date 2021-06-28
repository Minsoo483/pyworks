# 장바구니 클래스 만들기 - 인스턴스 리스트 변수

class Cart:
    li = []  # 클래스 리스트 변수 -> 누적 가능

    def __init__(self, goods):
        Cart.li.append(goods)

    def showinfo(self):
        print(self.li)


c1 = Cart("두부")
c1.showinfo()
c1 = Cart("계란")
c1.showinfo()
c1 = Cart("생선")
c1.showinfo()
