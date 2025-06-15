import tkinter
screen=tkinter.Tk()
screen.geometry("800x600")
screen.title("calander")
label=tkinter.Label(screen,text="calender",bg="Gray",fg="Black",font=("Arial",80,"bold"))
label1=tkinter.Label(screen,text="enter year",bg="Green",fg="Black",font=("Arial",20,))
entry=tkinter.Entry(screen,)
button=tkinter.Button(screen,text="show calender",bg="Red",fg="Black",font=("Arial",20))
button1=tkinter.Button(screen,text="EXIT",bg="Red",fg="Black",font=("Arial",20,"bold"))
label.pack()
label1.pack()
entry.pack()
button.pack()
button1.pack()



screen.mainloop()