from tkinter import *

window = Tk()
window.title("Calculator")

e=Entry(window,width=45, borderwidth=5)
e.grid(row=0, column=0,columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,  str(current) + str(number) )


def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0,END)
def button_equal():
    second_num = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num + int(second_num))
    if math == "subtraction":
        e.insert(0, f_num - int(second_num))
    if math == "multiplication":
        e.insert(0, f_num * int(second_num))
    if math == "division":
        e.insert(0, f_num / int(second_num))

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)
def button_ac():
    e.delete(0,END)

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)
def button_percentage():
   second_number = e.get()
   e.delete(0,END)
   if math =="multiplication":
       e.insert(0, f_num / 100 * int(second_number))
   if math =="division":
       e.insert(0, f_num * 100 / int(second_number))

def button_clear():
    e.delete(0,END)

# Define Buttons
button_ac = Button(window,text="AC",padx=41, pady=20,command = button_ac )
button_c = Button(window,text="C",padx=46, pady=20,command = button_clear)
button_pon = Button(window,text="+/-",padx=40, pady=20,command =button_add )
button_div = Button(window,text="/",padx=40, pady=20,command = button_divide )
button_mul = Button(window,text="X",padx=40, pady=20,command = button_multiply )
button_min = Button(window,text="-",padx=40, pady=20,command = button_subtract )
button_plus = Button(window,text="+",padx=40, pady=20,command = button_add )
button_equal = Button(window,text="=",padx=40, pady=20,command = button_equal)

button_7 = Button(window,text="7",padx=46, pady=20,command =lambda:button_click(7))
button_8 = Button(window,text="8",padx=46, pady=20,command = lambda:button_click(8) )
button_9 = Button(window,text="9",padx=46, pady=20,command = lambda:button_click(9) )
button_4 = Button(window,text="4",padx=46, pady=20,command = lambda:button_click(4) )
button_5 = Button(window,text="5",padx=46, pady=20,command = lambda:button_click(5) )
button_6 = Button(window,text="6",padx=46, pady=20,command = lambda:button_click(6) )
button_1 = Button(window,text="1",padx=46, pady=20,command = lambda:button_click(1) )
button_2 = Button(window,text="2",padx=46, pady=20,command = lambda:button_click(2) )
button_3 = Button(window,text="3",padx=46, pady=20,command = lambda:button_click(3) )
button_per = Button(window,text="%",padx=45, pady=20,command =button_percentage)
button_0 = Button(window,text="0",padx=46, pady=20,command = lambda:button_click(0) )
button_dot = Button(window,text=".",padx=47, pady=20,command = lambda:button_click(".") )

# Put Buttons on the screen
button_ac.grid(row=1,column=0)
button_c.grid(row=1,column=1)
button_pon.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_mul.grid(row=2,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_min.grid(row=3,column=3)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_plus.grid(row=4,column=3)

button_per.grid(row=5,column=0)
button_0.grid(row=5,column=1)
button_dot.grid(row=5,column=2)
button_equal.grid(row=5,column=3)
window.mainloop()