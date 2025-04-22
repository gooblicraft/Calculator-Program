#Added functionality and make it more neat for fewer lines of codes

from tkinter import *

def button_click(value):
    current = entry1.get()
    if current == "":
        entry1.delete(0, END)
        current = ""
    entry1.insert(END, str(value))

def clear_entry():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry1.insert(0, "")
    entry2.insert(0, "")

def calculate():
    try:
        result = eval(entry1.get())
        entry2.delete(0, END)
        entry2.insert(0, str(result))
    except:
        entry2.delete(0, END)
        entry2.insert(0, "Error")

mainWindow = Tk()
mainWindow.geometry('250x270')
mainWindow.title("Calculator Program")
mainWindow.resizable(FALSE, FALSE)

# Frame for entries
frame1 = Frame(mainWindow)
frame1.grid(row=0, column=0, padx=5)

# Entries
entry1 = Entry(frame1, font=("Helvetica", 12), justify=RIGHT, width=26)
entry1.grid(row=0, column=0)

entry2 = Entry(frame1, font=("Helvetica", 24), justify=RIGHT, width=13)
entry2.grid(row=1, column=0)

# Frame for buttons
frame2 = Frame(mainWindow)
frame2.grid(row=1, column=0, pady=5)

# Number and operation buttons
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        cmd = clear_entry
    elif text == '=':
        cmd = calculate
    else:
        cmd = lambda val=text: button_click(val)

    Button(frame2, text=text, font="Helvetica", width=4, height=2, command=cmd).grid(row=row, column=col, padx=8)

mainWindow.mainloop()
