from tkinter import *
import tkinter.font as tkFont

def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, text)

window = Tk()
window.geometry("350x500")
window.title("Unique Calculator")
window.configure(bg="#212121")

font = tkFont.Font(family="Helvetica", size=16, weight="bold")

entry = Entry(window, font=("Helvetica", 24), bg="#FFFFFF", fg="#000000", bd=10, relief=SUNKEN, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_colors = {
    'numbers': "#37474F",
    'operators': "#FFAB00",
    'clear': "#D32F2F"
}

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
    ('=',)
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text in {'/', '*', '-', '+', '='}:
            btn = Button(window, text=text, font=font, bg=button_colors['operators'], fg="#FFFFFF", width=5, height=2, relief=RAISED, borderwidth=2)
        elif text == 'C':
            btn = Button(window, text=text, font=font, bg=button_colors['clear'], fg="#FFFFFF", width=5, height=2, relief=RAISED, borderwidth=2)
        else:
            btn = Button(window, text=text, font=font, bg=button_colors['numbers'], fg="#FFFFFF", width=5, height=2, relief=RAISED, borderwidth=2)

        btn.grid(row=r+1, column=c, padx=5, pady=5)
        btn.bind("<Button-1>", click)

window.mainloop()