from tkinter import *
root = Tk()
root.geometry("700x1000")

def getvals():
    print("Сакланди")


Label(root, text="РЕКЛАМА АГЕНТЛИГИ ", bg='RED',fg='white', font="arial 24 bold").grid(row=0, column=3)


rek1 = Label(root, text="ТЕЛ. РАКАМ", fg='GREEN')
rek2 = Label(root, text="РЕКЛАМА ТУРИ", fg='GREEN')
when = Label(root, text="ТОЛАВ ТУРИ $", fg='GREEN')
ticketn = Label(root, text="РЕКЛАМА МУДАТИ", fg='GREEN')


rek1.grid(row=1, column=2)
rek2.grid(row=2, column=2)
when.grid(row=3, column=2)
ticketn.grid(row=4, column=2)


rek1value = StringVar
rek2value = StringVar
whenvalue = StringVar
ticketnvalue = StringVar
checkvalue = IntVar


rek1entry = Entry(root, textvariable =rek1value)
rek2entry = Entry(root, textvariable =rek2value)
whenentry = Entry(root, textvariable =whenvalue)
ticketnentry = Entry(root, textvariable=ticketnvalue)



rek1entry.grid(row=1, column=3)
rek2entry.grid(row=2, column=3)
whenentry.grid(row=3, column=3)
ticketnentry.grid(row=4, column=3)


checkbtn = Checkbutton(text="ЙОДДА САКЛАШ?")
checkbtn.grid(row=6, column=3)



Button(text="Саклаш", command=getvals, fg='white', bg='blue').grid(row=7, column=3)

root.mainloop()

