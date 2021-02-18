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
fontStyle = tkFont.Font(size=32, family="Courier", weight="bold")
fontStyle2 = tkFont.Font(size=25, family="Courier")
window_maths = Entry(root, width=10, borderwidth=0, bg="#f2f2f2", justify='right', font=fontStyle2)
window_maths.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=2)

window = Entry(root, width=10, borderwidth=0, bg="#f2f2f2", justify='right', font=fontStyle)
window.grid(row=1, column=0, columnspan=4, padx=20, pady=12, ipady=22)

# set default digit zero in the window
window.insert(0, 0)


# ---------THE LOGIC ------------------

# --------- THE MAIN LOGIC ------------
def button_click(number=None):
    if window.get() == '0':
        window.delete(0, END)
    current = window.get()
    window.delete(0, END)
    window.insert(0, f"{current}{number}")

    math_curr = window_maths.get()
    window_maths.delete(0, END)
    window_maths.insert(0, f"{math_curr}{current}{number}")


def button_clear(elem=None):
    window.delete(0, END)
    window_maths.delete(0, END)


def button_add(elem=None):
    first_number = window.get()
    global f_num
    global math
    math = "addition"
    f_num = check_decimal(first_number)
    window.delete(0, END)

    window_maths.delete(0, END)
    window_maths.insert(0, f"{first_number}+")


def button_subtract(elem=None):
    first_number = window.get()
    global f_num
    global math
    math = "substract"
    f_num = check_decimal(first_number)
    window.delete(0, END)

    window_maths.delete(0, END)
    window_maths.insert(0, f"{first_number}-")


def button_multiply(elem=None):
    first_number = window.get()
    global f_num
    global math
    math = "multiplication"
    f_num = check_decimal(first_number)
    window.delete(0, END)
    window_maths.delete(0, END)
    window_maths.insert(0, f"{first_number}x")


def button_devide(elem=None):
    first_number = window.get()
    global f_num
    global math
    math = "division"
    f_num = check_decimal(first_number)
    window.delete(0, END)
    window_maths.delete(0, END)
    window_maths.insert(0, f"{first_number}/")


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


def button_back(elem=None):
    first_number = window.get()
    backed = str(first_number)[:-1]
    global f_num
    f_num = check_decimal(backed)
    window.delete(0, END)
    window.insert(0, f_num)


def button_point(elem=None):
    first_number = window.get()
    f_num = f"{first_number}."

    window.delete(0, END)
    window.insert(0, f_num)


def button_plus_minus():
    first_number = window.get()
    backed = str(first_number)[0]
    global f_num
    if backed == '-':
        f_num = abs(check_decimal(first_number))
    else:
        f_num = check_decimal(f"-{(str(check_decimal(backed)))}")

    window.delete(0, END)
    window.insert(0, f_num)


def button_equal(elem=None):
    second_number = window.get()
    window.delete(0, END)
    result = 0
    if math == "addition":
        result = f_num + check_decimal(second_number)
    elif math == "substract":
        result = f_num - check_decimal(second_number)
    elif math == "multiplication":
        result = round(f_num * check_decimal(second_number), 10)
    elif math == "division":
        result = round(f_num / check_decimal(second_number), 10)

    window.insert(0, result)
    math_curr = window_maths.get()
    window_maths.delete(0, END)
    window_maths.insert(0, f"{math_curr}={result}")


def check_decimal(number):
    if len(number.split('.')) == 1:
        return int(number)
    else:
        # also check if input is for ex. <.1> instead of <0.1>
        if number.split('.')[0] == "":
            number = f"0{number}"
        return float(number)


# ----- KEYBOARD PRESS LOGIC------------

def one(digit=None):
    return button_click(1)


def two(digit):
    return button_click(2)


def three(digit):
    return button_click(3)


def four(digit):
    return button_click(4)


def five(digit):
    return button_click(5)


def six(digit):
    return button_click(6)


def seven(digit):
    return button_click(7)


def eight(digit):
    return button_click(8)


def nine(digit):
    return button_click(9)


def zero(digit):
    return button_click(0)


root.bind('1', one)
root.bind('2', two)
root.bind('3', three)
root.bind('4', four)
root.bind('5', five)
root.bind('6', six)
root.bind('7', seven)
root.bind('8', eight)
root.bind('9', nine)
root.bind('0', zero)

root.bind('+', button_add)
root.bind('-', button_subtract)
root.bind('/', button_devide)
root.bind('*', button_multiply)
root.bind('.', button_point)
root.bind('<Return>', button_equal)
root.bind('<Delete>', button_clear)
root.bind('<BackSpace>', button_back)

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

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_0.grid(row=7, column=1)

button_point.grid(row=7, column=2)
button_plus_minus.grid(row=7, column=0)

button_add.grid(row=6, column=3)
button_equal.grid(row=7, column=3)
button_clear.grid(row=2, column=2)
button_subtract.grid(row=5, column=3)
button_multiply.grid(row=4, column=3)
button_devide.grid(row=3, column=3)

button_fraction.grid(row=3, column=0)
button_pow.grid(row=3, column=1)
button_sqrt.grid(row=3, column=2)

button_back.grid(row=2, column=3)


# ---- BUTTON COLOR HOVER -----------------------

# function to change properties of button on hover
def changeOnHover(button, on_hover, on_leave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=on_hover))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=on_leave))


changeOnHover(button_1, "#8c929c", "white")
changeOnHover(button_2, "#8c929c", "white")
changeOnHover(button_3, "#8c929c", "white")
changeOnHover(button_4, "#8c929c", "white")
changeOnHover(button_5, "#8c929c", "white")
changeOnHover(button_6, "#8c929c", "white")
changeOnHover(button_7, "#8c929c", "white")
changeOnHover(button_8, "#8c929c", "white")
changeOnHover(button_9, "#8c929c", "white")
changeOnHover(button_0, "#8c929c", "white")

changeOnHover(button_point, "#8c929c", "#e6e9eb")
changeOnHover(button_plus_minus, "#8c929c", "#e6e9eb")
changeOnHover(button_add, "#8c929c", "#e6e9eb")
changeOnHover(button_equal, "#5285d9", "#9dbff5")
changeOnHover(button_clear, "#8c929c", "#e6e9eb")
changeOnHover(button_subtract, "#8c929c", "#e6e9eb")
changeOnHover(button_multiply, "#8c929c", "#e6e9eb")
changeOnHover(button_devide, "#8c929c", "#e6e9eb")
changeOnHover(button_fraction, "#8c929c", "#e6e9eb")
changeOnHover(button_pow, "#8c929c", "#e6e9eb")
changeOnHover(button_sqrt, "#8c929c", "#e6e9eb")
changeOnHover(button_back, "#8c929c", "#e6e9eb")

root.mainloop()
