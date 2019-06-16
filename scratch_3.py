import tkinter

lastx1, lasty1 = 0, 0
미친색 = "blue"
지금미친색= "파란색"

def scratch_goorimpan():
    paper = tkinter.Tk()
    paper.geometry("1000x1000+0+0")
    paper.resizable(1, 1)
    paper.title("그림판")

    def 인직(event):
        global lastx1, lasty1
        lastx1, lasty1 = event.x, event.y
        canvas.create_line(event.x, event.y, event.x + 1, event.y + 1, fill = 미친색, width = 3)

    def 정지호븽띤(event):
        global lastx1, lasty1
        canvas.create_line(lastx1, lasty1, event.x, event.y, fill = 미친색, width = 3)
        lastx1, lasty1 = event.x, event.y

    def 메인으로():
        paper.destroy()
        import scratch
        scratch()

    def 미친노랑():
        global 미친색, 지금미친색
        미친색 = "yellow"
        지금미친색 = "노란색"
        지금개미친색.config(text = "지금의 개미친색깔은? →  " + str(지금미친색))

    def 미친초록():
        global 미친색, 지금미친색
        미친색 = "green"
        지금미친색 = "초록색"
        지금개미친색.config(text="지금의 개미친색깔은? →  " + str(지금미친색))


    def 미친검정():
        global 미친색, 지금미친색
        미친색 = "black"
        지금미친색 = "검정색"
        지금개미친색.config(text="지금의 개미친색깔은? →  " + str(지금미친색))

    def 미친지우개():
        global 미친색, 지금미친색
        미친색 = "white"
        지금미친색 = "지우개"
        지금개미친색.config(text="지금의 개미친색깔은? →  " + str(지금미친색))

    def 으악():
        canvas.delete("all")

    테두리버억 = tkinter.Frame(paper, width = 600, height = 400, relief = "solid", bd = 2)
    테두리버억.place(x=1, y=1)

    canvas = tkinter.Canvas(테두리버억, width=600, height=400, cursor="pencil",bg="white", bd=5)

    지금개미친색 = tkinter.Label(paper, text="지금의 개미친색깔은? →  " + 지금미친색)
    지금개미친색.place(x=400, y=500)




    메인화면으로띠용 = tkinter.Button(paper, overrelief="solid", width=20, command=메인으로, repeatdelay=1, repeatinterval=100,
                              activebackground="black", height=20, text="메인으로 내다 가버려", bd=3)
    메인화면으로띠용.place(x=1, y=700)

    미친색깔놀이 = tkinter.Button(paper, overrelief="solid", width=10, command=미친노랑, repeatdelay=1, repeatinterval=100,
                            activebackground="yellow", height=10, text="미친 노란색", bd=3)
    미친색깔놀이.place(x=200, y=700)

    미친색깔놀이2 = tkinter.Button(paper, overrelief="solid", width=10, command=미친초록, repeatdelay=1, repeatinterval=100,
                             activebackground="green", height=10, text="미친 초록색", bd=3)
    미친색깔놀이2.place(x=300, y=700)

    미친색깔놀이3 = tkinter.Button(paper, overrelief="solid", width=10, command=미친검정, repeatdelay=1, repeatinterval=100,
                             activebackground="black", height=10, text="미친 검은색", bd=3)
    미친색깔놀이3.place(x=400, y=700)

    미친초기화 = tkinter.Button(paper, overrelief="solid", width=10, command=으악, repeatdelay=1, repeatinterval=100,
                           activebackground="blue", height=5, text="미친 초기화", bd=3)
    미친초기화.place(x=700, y=300)

    미친지우개 = tkinter.Button(paper, overrelief="solid", width=10, command=미친지우개, repeatdelay=1, repeatinterval=100,
                           activebackground="white", height=10, text="미친 지우개", bd=3)
    미친지우개.place(x=500, y=700)

    canvas.bind("<B1-Motion>", 정지호븽띤)
    canvas.bind("<Button-1>", 인직)
    canvas.pack()

    paper.mainloop()