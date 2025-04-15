#Calculator Program in Quiz 1.B in ITCS 102 using only grid

from tkinter import *

mainWindow = Tk()
mainWindow.geometry('250x270')
mainWindow.title("Calculator Program")
mainWindow.resizable(FALSE, FALSE) #Fix window, cannot be resize

#Frame for entry1 and entry2
frame1 = Frame(mainWindow)
frame1.grid(row=0, column=0, padx=5)

#Entries
entry1 = Entry(frame1, font=("Helvetica",12), justify=RIGHT, width=26)
entry1.insert(1, "Operations")
entry1.grid(row=0, column=0)

entry2 = Entry(frame1, font=("Helvetica",24), justify=RIGHT,width=13)
entry2.insert(2, "Result")
entry2.grid(row=1, column=0)

#Frame for buttons number and operators
frame2 = Frame(mainWindow)
frame2.grid(row=1, column=0, pady=5)

#Buttons
button7 = Button(frame2, text="7", font="Helvetica", width=4, height=2)
button7.grid(row=0, column=0, padx=8)

button8 = Button(frame2, text="8", font="Helvetica", width=4, height=2)
button8.grid(row=0, column=1, padx=8)

button9 = Button(frame2, text="9", font="Helvetica", width=4, height=2)
button9.grid(row=0, column=2, padx=8)

buttonDivide = Button(frame2, text="/", font="Helvetica", width=4, height=2)
buttonDivide.grid(row=0, column=3,padx=8)

button4 = Button(frame2, text="4", font="Helvetica", width=4, height=2)
button4.grid(row=1, column=0, padx=8)

button4 = Button(frame2, text="5", font="Helvetica", width=4, height=2)
button4.grid(row=1, column=1, padx=8)

button4 = Button(frame2, text="6", font="Helvetica", width=4, height=2)
button4.grid(row=1, column=2, padx=8)

buttonMultiply = Button(frame2, text="*", font="Helvetica", width=4, height=2)
buttonMultiply.grid(row=1, column=3, padx=8)

button1 = Button(frame2, text="1", font="Helvetica", width=4, height=2)
button1.grid(row=2, column=0, padx=8)

button2 = Button(frame2, text="2", font="Helvetica", width=4, height=2)
button2.grid(row=2, column=1, padx=8)

button3 = Button(frame2, text="3", font="Helvetica", width=4, height=2)
button3.grid(row=2, column=2, padx=8)

buttonMinus = Button(frame2, text="-", font="Helvetica", width=4, height=2)
buttonMinus.grid(row=2, column=3, padx=8)

buttonDelete = Button(frame2, text="C", font="Helvetica", width=4, height=2)
buttonDelete.grid(row=3, column=0, padx=8)

buttonZero = Button(frame2, text="0", font="Helvetica", width=4, height=2)
buttonZero.grid(row=3, column=1, padx=8)

buttonEqual = Button(frame2, text="=", font="Helvetica", width=4, height=2)
buttonEqual.grid(row=3, column=2, padx=8)

buttonAdd = Button(frame2, text="+", font="Helvetica", width=4, height=2)
buttonAdd.grid(row=3, column=3, padx=8)

#Test
mainWindow.mainloop()