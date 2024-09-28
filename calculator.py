from tkinter import *



root = Tk()
root.title('simple calculator')
root.iconbitmap("calc icon.ico") #changes the title icon


enter = Entry(root, width=25, borderwidth=5)
enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



def button_click(number):
    current = enter.get()
    enter.delete(0, END)
    enter.insert(0, str(current) + str(number))

def button_clear():
    enter.delete(0, END)

def button_add():
    first_number=enter.get()
    global f_num #global variable to make the calculations for the buttons
    global math
    math = 'addition'
    f_num=int(first_number)
    enter.delete(0, END)

def button_subtract():
    first_number = enter.get()
    global f_num  # global variable to make the calculations for the buttons
    global math
    math = 'subtraction'
    f_num = int(first_number)
    enter.delete(0, END)

def button_multiply():
    first_number = enter.get()
    global f_num  # global variable to make the calculations for the buttons
    global math
    math = 'multiply'
    f_num = int(first_number)
    enter.delete(0, END)

def button_divide():
    first_number = enter.get()
    global f_num  # global variable to make the calculations for the buttons
    global math
    math = 'divide'
    f_num = int(first_number)
    enter.delete(0, END)

def button_equal():
    second_number=enter.get()
    enter.delete(0, END)
    if math == 'addition':
        enter.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        enter.insert(0, f_num - int(second_number))
    elif math == "multiply":
        enter.insert(0, f_num * int(second_number))
    elif math == "divide":
        enter.insert(0, f_num / int(second_number))

#lambda is for allowing button functions to take in the brackets

button1 = Button(root, text ='1', padx =40, pady=20,command=lambda :button_click(1))
button2 = Button(root, text ='2', padx =40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text ='3', padx =40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text ='4', padx =40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text ='5', padx =40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text ='6', padx =40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text ='7', padx =40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text ='8', padx =40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text ='9', padx =40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text ='0', padx =40, pady=20, command=lambda: button_click(0))
button_equal = Button(root, text='=', padx=40, pady=20,bg="#1591ea", command=button_equal)
button_clear = Button(root, text='c', padx=40, pady=20, command=button_clear)

button_add = Button(root, text ='+', padx=40, pady=20,bg="#546373", command=button_add)
button_subtract = Button(root, text ='-', padx=40, pady=20, bg="#546373", command=button_subtract)
button_multiply = Button(root, text ='x', padx=40, pady=20, bg="#546373", command=button_multiply)
button_divide = Button(root, text ='/', padx=40, pady=20, bg="#546373", command=button_divide)

#putting the buttons on screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_add.grid(row=3,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_multiply.grid(row=2,column=3)


button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_divide.grid(row=1,column=3)

button_clear.grid(row=4,column=0)
button0.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_subtract.grid(row=4,column=3)

root.mainloop()