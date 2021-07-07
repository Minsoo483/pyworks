from tkinter import *


def click():
    print("Hello~ Python!!")


root = Tk()
root.title("Hello~")

frame = Frame(root)
frame.pack()

Button(frame, text='확인', command=click).grid(row=0 ,column=0)
# click()가로를 빼는 이유는 버튼 누를때만 함수가 작동하도록 하기 위해서!
# ()가 있으면 함수 생성시점에서 동작


root.mainloop()