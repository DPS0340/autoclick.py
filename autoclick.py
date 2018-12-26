import win32api
import win32con
import time
from tkinter import *

def click(x,y,n):
    for i in range(n):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.005)

def find():
    return [win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]]
    time.sleep(0.01)





def main():
    root = Tk()
    xinput = StringVar()
    yinput = StringVar()
    numberinput = StringVar()

    def update_x1y1():
        while(True):
            x1.config(text=str(find()[0]))
            y1.config(text=str(find()[1]))
            root.update()

    def run():
        x = int(xinput.get())
        y = int(yinput.get())
        n = int(numberinput.get())
        click(x,y,n)

    label1 = Label(root, text="현재 좌표")
    label1.grid(row=0, column=0)
    x1 = Label(root, text="None")
    x1.grid(row=0, column=1)
    y1 = Label(root, text="None")
    y1.grid(row=0, column=2)
    btn1 = Button(root, text="좌표 찾기", width=15, command=update_x1y1)
    btn1.grid(row=0, column=3)


    label2 = Label(root, text="좌표 입력")
    label2.grid(row=1, column=0)
    x2 = Entry(root, textvariable=xinput)
    x2.grid(row=1, column=1)
    y2 = Entry(root, textvariable=yinput)
    y2.grid(row=1, column=2)
    label3 = Label(root, text="횟수 입력")
    label3.grid(row=2, column=0)
    number = Entry(root, textvariable=numberinput)
    number.grid(row=2, column=1)
    btn2 = Button(root, text="확인", width=15, command=run)
    btn2.grid(row=2, column=3)

    root.mainloop()

main()
