import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("300x300")
root.title("Welcome to a simple calculator")

label = tk.Label(root, text="A simple Calculator", font=("Arial", 12))
label.pack(padx=10, pady=10)

display = tk.StringVar(value="")
screen = tk.Entry(root, font=("Arial", 12), width=30, textvariable=display)
screen.pack()
num1=None
o=None

def adddigits(d):
    now=display.get()
    if now=="":
        display.set(str(d))
    else:
        display.set(now+str(d))
def adddecimal():
    current=display.get()
    if o and (o in current):
        end=current.split(o)[-1]
    else:
        end=current
    if "." not in end:
        display.set(current + ".")



def click_operator(symbol):
    global num1,o
    num1=float(display.get())
    o=symbol
    display.set(display.get()+symbol)
    
def click_equals():
    global num1,o
    e=display.get()
    if o in e:
        num2=float(e.split(o)[1])
    else:
        return
    if o=="//":
        answer=num1//num2
        
    elif o=="+":
        answer=num1+num2
    elif o=="-":
        answer=num1-num2
    elif o=="*":
        answer=num1*num2
    elif o=="%":
        if num2==0:
            from tkinter import messagebox
            messagebox.showwarning(message="Cannot modulo divide by 0")
            display.set("")
            num1=None
            o=None
            return
        else:
            answer=num1%num2
    elif o=="/":
        if num2==0:
            from tkinter import messagebox
            messagebox.showwarning(title="Error",message="Cannot divide by 0")
            display.set("")
            num1=None
            o=None
            return
        else:
            answer=num1/num2
    elif o=="//":
        answer=num1//num2
    display.set(str(answer))
    num1=None
    o=None

def click_clear():
    display.set("")

def closing():
    m=messagebox.askyesnocancel("Exit", "Do you want to exit from our calculator?")
    if m is True:
        root.destroy()
def clearcurrent():
    s=display.get()
    l=list(s)
    last=l[-1]
    l.remove(last)
    new_str="".join(l)
    display.set(new_str)
    


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

buttonframe.rowconfigure(0, weight=1)
buttonframe.rowconfigure(1, weight=1)
buttonframe.rowconfigure(2, weight=1)
buttonframe.rowconfigure(3, weight=1)
buttonframe.rowconfigure(4, weight=1)

b1 = tk.Button(buttonframe, text=1, font=("Arial", 10), command=lambda: adddigits(1))
b1.grid(row=0, column=0, sticky="news", padx=5, pady=5)

b2 = tk.Button(buttonframe, text=2, font=("Arial", 10), command=lambda: adddigits(2))
b2.grid(row=0, column=1, sticky="news", padx=5, pady=5)

b3 = tk.Button(buttonframe, text=3, font=("Arial", 10), command=lambda: adddigits(3))
b3.grid(row=0, column=2, sticky="news", padx=5, pady=5)

b4 = tk.Button(buttonframe, text=4, font=("Arial", 10), command=lambda: adddigits(4))
b4.grid(row=1, column=0, sticky="news", padx=5, pady=5)

b5 = tk.Button(buttonframe, text=5, font=("Arial", 10), command=lambda: adddigits(5))
b5.grid(row=1, column=1, sticky="news", padx=5, pady=5)

b6 = tk.Button(buttonframe, text=6, font=("Arial", 10), command=lambda: adddigits(6))
b6.grid(row=1, column=2, sticky="news", padx=5, pady=5)

b7 = tk.Button(buttonframe, text=7, font=("Arial", 10), command=lambda: adddigits(7))
b7.grid(row=2, column=0, sticky="news", padx=5, pady=5)

b8 = tk.Button(buttonframe, text=8, font=("Arial", 10), command=lambda: adddigits(8))
b8.grid(row=2, column=1, sticky="news", padx=5, pady=5)

b9 = tk.Button(buttonframe, text=9, font=("Arial", 10), command=lambda: adddigits(9))
b9.grid(row=2, column=2, sticky="news", padx=5, pady=5)

b10 = tk.Button(buttonframe, text=0, font=("Arial", 10), command=lambda: adddigits(0))
b10.grid(row=0, column=3, sticky="news", padx=5, pady=5)

b11 = tk.Button(buttonframe, text="+", font=("Arial", 10), command=lambda: click_operator("+"))
b11.grid(row=1, column=3, sticky="news", padx=5, pady=5)

b12 = tk.Button(buttonframe, text="-", font=("Arial", 10), command=lambda: click_operator("-"))
b12.grid(row=2, column=3, sticky="news", padx=5, pady=5)

b13 = tk.Button(buttonframe, text="*", font=("Arial", 10), command=lambda: click_operator("*"))
b13.grid(row=3, column=3, sticky="news", padx=5, pady=5)

b14 = tk.Button(buttonframe, text="/", font=("Arial", 10), command=lambda: click_operator("/"))
b14.grid(row=3, column=0, sticky="news", padx=5, pady=5)

b15 = tk.Button(buttonframe, text="%", font=("Arial", 10), command=lambda: click_operator("%"))
b15.grid(row=3, column=1, sticky="news", padx=5, pady=5)

b16 = tk.Button(buttonframe, text="=", font=("Arial", 10), command=lambda: click_equals())
b16.grid(row=3, column=2, sticky="news", padx=5, pady=5)

b17 = tk.Button(buttonframe, text="//", font=("Arial", 10), command=lambda:click_operator("//"))
b17.grid(row=4, column=2, sticky="news", padx=5, pady=5)

b18 = tk.Button(buttonframe, text=".", font=("Arial", 10), command=lambda:adddecimal())
b18.grid(row=4, columnspan=2, sticky="news", padx=5, pady=5)

b_clear = tk.Button(buttonframe, text="Clear", font=("Arial", 10), command=lambda: click_clear())
b_clear.grid(row=4, columnspan=2, sticky="news", padx=5, pady=5)

b_clearcurrent = tk.Button(buttonframe, text="X", font=("Arial", 10), command=lambda: clearcurrent())
b_clearcurrent.grid(row=4, column=3, sticky="news", padx=5, pady=5)
buttonframe.pack(expand=True, fill="both")
root.protocol("WM_DELETE_WINDOW", closing)
root.mainloop()