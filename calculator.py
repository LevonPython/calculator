from tkinter import *
import tkinter.font as tkFont
import math
import os


# ---------- CALCULATOR WINDOW CREATING----------
root = Tk()
root.title("Standard calculator")
# path = os.path.abspath(os.getcwd())
# print(path)
# full_path = os.path.join(path, "pow.jpg")
# print(full_path)

window = Entry(root, width=35, borderwidth=1)
window.grid(row=0, column=0, columnspan=4, padx=53, pady=80)
# window.insert(0, "Insert your name")


# --------- THE LOGIC ------------
def button_click(number):
    # window.delete(0, END)
    current = window.get()
    window.delete(0, END)
    window.insert(0, f"{current}{number}")


def button_clear():
    window.delete(0, END)


def button_add():
    first_number = window.get()
    global f_num
    global math
    math = "addition"
    f_num = check_decimal(first_number)
    window.delete(0, END)


def button_subtract():
    first_number = window.get()
    global f_num
    global math
    math = "substract"
    f_num = check_decimal(first_number)
    window.delete(0, END)


def button_multiply():
    first_number = window.get()
    global f_num
    global math
    math = "multiplication"
    f_num = check_decimal(first_number)
    window.delete(0, END)


def button_devide():
    first_number = window.get()
    global f_num
    global math
    math = "division"
    f_num = check_decimal(first_number)
    window.delete(0, END)


def button_fraction():
    first_number = window.get()
    window.delete(0, END)
    window.insert(0, 1/int(first_number))


def button_pow():
    first_number = int(window.get())
    window.delete(0, END)
    window.insert(0, round(math.pow(first_number, 2)))


def button_sqrt():
    first_number = int(window.get())
    window.delete(0, END)
    window.insert(0, round(math.sqrt(first_number)))


def button_back():
    first_number = window.get()
    backed = str(first_number)[:-1]
    global f_num
    f_num = check_decimal(backed)
    window.delete(0, END)
    window.insert(0, f_num)

def button_point():
    return


def button_plus_minus():
    first_number = window.get()
    backed = str(first_number)[0]
    global f_num
    if backed == '-':
        f_num = abs(check_decimal(backed))
    else:
        f_num = (check_decimal(backed))

    window.delete(0, END)
    window.insert(0, f_num)


def button_equal():
    second_number = window.get()
    window.delete(0, END)

    if math == "addition":
        window.insert(0, f_num + int(second_number))
    elif math == "substract":
        window.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        window.insert(0, f_num * int(second_number))
    elif math == "division":
        window.insert(0, f_num / int(second_number))


def check_decimal(number):
    if len(number.split('.')) == 1:
        return int(number)
    else:
        return float(number)


# --------- THE INTERFACE ------------
# button text font styles
fontStyle = tkFont.Font(size=13, weight="bold")
fontStyle2 = tkFont.Font(size=17)
fontStyle3 = tkFont.Font(size=13)

# Define buttons

button_1 = Button(root, text="1", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=29, pady=11, bg='white', bd=0, font=fontStyle, command=lambda: button_click(0))

button_point = Button(root, text=".", padx=31, pady=11, bg='white', bd=0, font=fontStyle, command=button_point)
button_plus_minus = Button(root, text="+/-", padx=24, pady=11, bg='white', bd=0, font=fontStyle, command=button_plus_minus)

button_add = Button(root, text="+", padx=26, pady=5, bg='#e6e9eb', bd=0, font=fontStyle2, command=button_add)
button_equal = Button(root, text="=", padx=26, pady=5, bd=0, bg='#9dbff5', font=fontStyle2, command=button_equal)
button_clear = Button(root, text="c", padx=26, pady=5, bg='#e6e9eb', bd=0, font=fontStyle2, command=button_clear)

button_subtract = Button(root, text="-", padx=28, pady=5, bg='#e6e9eb', bd=0, font=fontStyle2, command=button_subtract)
button_multiply = Button(root, text="x", padx=26, pady=5, bg='#e6e9eb', bd=0, font=fontStyle2, command=button_multiply)
button_devide = Button(root, text="/", padx=29, pady=5, bg='#e6e9eb', bd=0, font=fontStyle2, command=button_devide)

button_fraction = Button(root, text="1/x", padx=23, pady=11, bg='#e6e9eb', bd=0, font=fontStyle3, command=button_fraction)
button_pow = Button(root, text="Pow", padx=18, pady=11, bg='#e6e9eb', bd=0, font=fontStyle3, command=button_pow)
button_sqrt = Button(root, text="Sqrt", padx=20, pady=11, bg='#e6e9eb', bd=0, font=fontStyle3, command=button_sqrt)

button_back = Button(root, text="Back", padx=16, pady=12, bg='#e6e9eb', bd=0, font=fontStyle3, command=button_back)

# Put the buttons on the screen

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=6, column=1)

button_point.grid(row=6, column=2)
button_plus_minus.grid(row=6, column=0)

button_add.grid(row=5, column=3)
button_equal.grid(row=6, column=3)
button_clear.grid(row=1, column=2)
button_subtract.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_devide.grid(row=2, column=3)

button_fraction.grid(row=2, column=0)
button_pow.grid(row=2, column=1)
button_sqrt.grid(row=2, column=2)

button_back.grid(row=1, column=3)

root.mainloop()
