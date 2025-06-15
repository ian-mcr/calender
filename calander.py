import tkinter
import calendar
screen=tkinter.Tk()
screen.geometry("800x600")
screen.title("calander")

def show():
    year=int(entry.get())
    screen1=tkinter.Tk()
    screen1.geometry("800x800")
    screen1.title("show calander")
    date=tkinter.Text(screen1,height=50)
    date.pack()
    calendardata=calendar.calendar(year)
    date.insert(tkinter.END,calendardata)
    screen1.mainloop()

def exit():
    screen.destroy()

label=tkinter.Label(screen,text="calender",bg="Gray",fg="Black",font=("Arial",80,"bold"))
label1=tkinter.Label(screen,text="enter year",bg="Green",fg="Black",font=("Arial",20,))
entry=tkinter.Entry(screen,width=40)
button=tkinter.Button(screen,text="show calender",bg="Red",fg="Black",command=show,font=("Arial",20))
button1=tkinter.Button(screen,text="EXIT",bg="Red",fg="Black",command=exit,font=("Arial",20,"bold"))
label.pack()
label1.pack()
entry.pack()
button.pack()
button1.pack()




screen.mainloop()