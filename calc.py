from tkinter import *
root=Tk()

root.geometry("500x750")
root.title("Calculator")
#root.wm_iconbitmap("lk.ico")
def click(event):
    global scval
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scval.get().isdigit():
            value=int(scval.get())
        else:
            try:
                value=eval(scval.get())
            except Exception as h:
                print(h)
                value="error"

        scval.set(value)
        #output.update()
    elif text=="C":
        value=""
        scval.set(value)
        #output.update()
    else:
        scval.set(scval.get()+text)
        
        #output.update()

scval=StringVar()
scval.set("")

output=Entry(root,textvariable=scval,font="Montserrat 25 bold").pack(pady=15)

# btn=[9,8,7,6,5,4,3,2,1,0]
#print(btn.index(7))

numbers = ["C", "/", "*", "+", "9", "8", "7", "-", "6", "5", "4", "(", "3", "2", "1", ")", ".", "0", ".", "="]

for i in range(0, len(numbers), 4):
    f1 = Frame(root, bg="grey")
    for j in range(4):
        index = i + j
        if index < len(numbers):
            b = Button(f1, text=numbers[index], padx=24, pady=24, font="Montserrat 20 bold")
            b.bind('<Button-1>',click)
            b.pack(side=LEFT, padx=12, pady=12)
            
    f1.pack()
root.mainloop()
