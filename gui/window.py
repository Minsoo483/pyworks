from tkinter import *

root = Tk() # TK클래스의 객체 생성
root.title("window")
root.geometry("200x100+300+400") # width x height + x좌표 + y좌표

frame = Frame(root) # root 위에 위치하는 프레임 객체 생성
frame.pack() # 레이아웃 담당하는 메소드


Label(frame, text="Hello Python").grid(row = 0, column =0)
Button(frame, text="확인").grid(row =1 , column =0)


root.mainloop()