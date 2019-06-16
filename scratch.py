import tkinter


window = tkinter.Tk()
window.title("이승재가 만든 개씹오지는 윈도우 창")
window.geometry("1920x400+0+0")
window.resizable(1, 1)

count = 0


def countUP1():
    global count
    count += 1
    label.config(text=str(count))


def countUP():
    global count
    count *= 2
    label.config(text=str(count))


def countUP3():
    global count
    count = 0
    label.config(text=str(count))

def getout():
    window.destroy()

def anggi_motti():
    from scratch_1 import scratch_function
    window.destroy()
    scratch_function()

def goorimpan():
    from scratch_3 import scratch_goorimpan
    window.destroy()
    scratch_goorimpan()

label시대 = tkinter.Label(window, text="시대를 뛰어넘는 코딩 실력")
label시대.pack()

label냅다 = tkinter.Label(window, text="버튼을 냅다 눌러")
label냅다.pack()

label = tkinter.Label(window, text="이승재의 쌉지리는 코드")
label.pack()


button1 = tkinter.Button(window, overrelief="solid", width=40, command=countUP1, repeatdelay=1, repeatinterval=100,
                         activebackground="red", height=10, text = "더하기 1")
button1.place(x=500, y=100)

button2 = tkinter.Button(window, overrelief="solid", width=40, command=countUP, repeatdelay=1, repeatinterval=100,
                         activebackground="blue", height=10, text = "곱하기 2")
button2.place(x=1100, y=100)

button3 = tkinter.Button(window, overrelief="solid", width=40, command=countUP3, repeatdelay=1, repeatinterval=100,
                         activebackground="black", text = "초기화")
button3.place(x=800, y=300)

button4 = tkinter.Button(window, overrelief="solid", width=30, command=getout, repeatdelay=1, repeatinterval=100,
                         activebackground="black", text = "밖으로 런")
button4.place(x=1600, y=100)

button5 = tkinter.Button(window, overrelief="solid", width=50, command=anggi_motti, repeatdelay=1, repeatinterval=100,
                         activebackground="black", text = "돼지 그림으로")
button5.place(x=1, y=350)

button6 = tkinter.Button(window, height= 10, width=20, command=goorimpan, repeatdelay=10, activebackground="yellow",
                         text = "이승재의 그림판 쌉지림")
button6.place(x=10, y=5)




window.mainloop()