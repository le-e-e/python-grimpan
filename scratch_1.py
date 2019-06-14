import tkinter


def scratch_function():
    root = tkinter.Tk()
    root.title("이승재가 만든 개씹오지는 윈도우 창")
    root.geometry("800x800+0+0")
    root.resizable(1, 1)

    def getout_1():
        root.destroy()
        import scratch
        scratch()

    button = tkinter.Button(root, overrelief="solid", width=40, command=getout_1, repeatdelay=1, repeatinterval=100,
                            activebackground="black", height=10, text="돌아가기")
    button.place(x=200, y=400)

    image = tkinter.PhotoImage(file="giphy.gif")

    label = tkinter.Label(root, image=image)
    label.pack()

    label = tkinter.Label(root, text="시대를 뛰어넘는 코딩 실력")
    label.pack()



    root.mainloop()