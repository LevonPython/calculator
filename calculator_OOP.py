from tkinter import *
import tkinter.font as tkFont
import math
import os


class Base:

    def __init__(self):
        self.root = Tk()
        self.root.title("Standard calculator")

        # self.windowSTYLES
        self.fontStyle = tkFont.Font(size=32, family="Courier", weight="bold")
        self.fontStyle2 = tkFont.Font(size=18, family="Courier")

        # WINDOWS
        self.window_maths = Entry(self.root, width=10, borderwidth=0, bg="#f2f2f2", justify='right',
                                  font=self.fontStyle2)
        self.window_maths.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=20, ipady=2)

        self.window = Entry(self.root, width=10, borderwidth=0, bg="#f2f2f2", justify='right', font=self.fontStyle)
        self.window.grid(row=1, column=0, columnspan=4, padx=20, pady=12, ipady=22)

        # set default digit zero in the window
        self.window.delete(0, 0)

        # BUTTON STYLES
        self.fontStyle = tkFont.Font(size=13, weight="bold")
        self.fontStyle2 = tkFont.Font(size=17)
        self.fontStyle3 = tkFont.Font(size=13)

    # --------- THE MAIN LOGIC ------------
    def button_click(self, number=None):
        if self.window.get() in ('0', 'x', '+', '-', '/'):
            self.window.delete(0, END)
        current = self.window.get()
        self.window.delete(0, END)
        self.window.insert(0, f"{current}{number}")
        math_curr = self.window_maths.get()
        self.window_maths.delete(0, END)
        self.window_maths.insert(0, f"{math_curr}{number}")

    def button_clear(self, elem=None):
        self.window.delete(0, END)
        self.window_maths.delete(0, END)
        self.window.insert(0, 0)

    def double_check(self, sign):
        return sign in ('x', '+', '-', '/')

    def button_add(self, elem=None):
        first_number = self.window.get()
        global f_num
        global math
        math = "addition"
        if not self.double_check(first_number):
            f_num = self.check_decimal(first_number)
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{first_number}+")
        else:
            sign_replace = self.window_maths.get()
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{sign_replace[:-1]}+")
        self.window.delete(0, END)
        self.window.insert(0, "+")

    def button_subtract(self, elem=None):
        first_number = self.window.get()
        global f_num
        global math
        math = "substract"
        if not self.double_check(first_number):
            f_num = self.check_decimal(first_number)
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{first_number}-")
        else:
            sign_replace = self.window_maths.get()
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{sign_replace[:-1]}-")
        self.window.delete(0, END)
        self.window.insert(0, "-")

    def button_multiply(self, elem=None):
        first_number = self.window.get()
        global f_num
        global math
        math = "multiplication"
        if not self.double_check(first_number):
            f_num = self.check_decimal(first_number)
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{first_number}x")
        else:
            sign_replace = self.window_maths.get()
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{sign_replace[:-1]}*")
        self.window.delete(0, END)
        self.window.insert(0, "x")

    def button_devide(self, elem=None):
        first_number = self.window.get()
        global f_num
        global math
        math = "division"
        if not self.double_check(first_number):
            f_num = self.check_decimal(first_number)
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{first_number}/")
        else:
            sign_replace = self.window_maths.get()
            self.window_maths.delete(0, END)
            self.window_maths.insert(0, f"{sign_replace[:-1]}/")
        self.window.delete(0, END)
        self.window.insert(0, "/")

    def button_fraction(self):
        first_number = self.window.get()
        self.window.delete(0, END)
        self.window.insert(0, 1 / int(first_number))

    def button_pow(self):
        first_number = int(self.window.get())
        self.window.delete(0, END)
        self.window.insert(0, round(math.pow(first_number, 2)))

    def button_sqrt(self):
        first_number = int(self.window.get())
        self.window.delete(0, END)
        self.window.insert(0, round(math.sqrt(first_number)))

    def button_back(self, elem=None):
        first_number = self.window.get()
        backed = str(first_number)[:-1]
        global f_num
        f_num = self.check_decimal(backed)
        self.window.delete(0, END)
        self.window.insert(0, f_num)

    def button_point(self, elem=None):
        first_number = self.window.get()
        f_num = f"{first_number}."
        self.window.delete(0, END)
        self.window.insert(0, f_num)

    def button_plus_minus(self):
        first_number = self.window.get()
        backed = str(first_number)[0]
        global f_num
        if backed == '-':
            f_num = abs(self.check_decimal(first_number))
        else:
            f_num = self.check_decimal(f"-{(str(self.check_decimal(backed)))}")
        self.window.delete(0, END)
        self.window.insert(0, f_num)

    def button_equal(self, elem=None):
        second_number = self.window.get()
        self.window.delete(0, END)
        result = 0
        global f_num
        if math == "addition":
            result = f_num + self.check_decimal(second_number)
        elif math == "substract":
            result = f_num - self.check_decimal(second_number)
        elif math == "multiplication":
            result = round(f_num * self.check_decimal(second_number), 10)
        elif math == "division":
            result = round(f_num / self.check_decimal(second_number), 10)
        self.window.insert(0, result)
        math_curr = self.window_maths.get()
        self.window_maths.delete(0, END)
        self.window_maths.insert(0, f"{math_curr}={result}")

    def check_decimal(self, number):
        if len(number.split('.')) == 1:
            return int(number)
        else:
            # also check if input is for ex. <.1> instead of <0.1>
            if number.split('.')[0] == "":
                number = f"0{number}"
            return float(number)

    def changeOnHover(self, button, on_hover, on_leave):
        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=on_hover))
        # background color on leaving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=on_leave))

    # KEYBOARD PRESS LOGIC
    def press(self, digit=None):
        return self.button_click(digit)


    def main(self):
        # --------- THE INTERFACE ------------
        # BUTTONS
        button_1 = Button(self.root, text="1", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(1))
        button_2 = Button(self.root, text="2", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(2))
        button_3 = Button(self.root, text="3", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(3))
        button_4 = Button(self.root, text="4", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(4))
        button_5 = Button(self.root, text="5", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(5))
        button_6 = Button(self.root, text="6", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(6))
        button_7 = Button(self.root, text="7", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(7))
        button_8 = Button(self.root, text="8", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(8))
        button_9 = Button(self.root, text="9", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(9))
        button_0 = Button(self.root, text="0", padx=29, pady=11, bg='white', bd=0, font=self.fontStyle,
                          command=lambda: self.button_click(0))
        button_point = Button(self.root, text=".", padx=31, pady=11, bg='white', bd=0, font=self.fontStyle,
                              command=self.button_point)
        button_plus_minus = Button(self.root, text="+/-", padx=24, pady=11, bg='white', bd=0, font=self.fontStyle,
                                   command=self.button_plus_minus)
        button_add = Button(self.root, text="+", padx=26, pady=5, bg='#e6e9eb', bd=0, font=self.fontStyle2,
                            command=self.button_add)
        button_equal = Button(self.root, text="=", padx=26, pady=5, bd=0, bg='#9dbff5', font=self.fontStyle2,
                              command=self.button_equal)
        button_clear = Button(self.root, text="c", padx=26, pady=5, bg='#e6e9eb', bd=0, font=self.fontStyle2,
                              command=self.button_clear)
        button_subtract = Button(self.root, text="-", padx=28, pady=5, bg='#e6e9eb', bd=0, font=self.fontStyle2,
                                 command=self.button_subtract)
        button_multiply = Button(self.root, text="x", padx=26, pady=5, bg='#e6e9eb', bd=0, font=self.fontStyle2,
                                 command=self.button_multiply)
        button_devide = Button(self.root, text="/", padx=29, pady=5, bg='#e6e9eb', bd=0, font=self.fontStyle2,
                               command=self.button_devide)
        button_fraction = Button(self.root, text="1/x", padx=23, pady=11, bg='#e6e9eb', bd=0, font=self.fontStyle3,
                                 command=self.button_fraction)
        button_pow = Button(self.root, text="Pow", padx=18, pady=11, bg='#e6e9eb', bd=0, font=self.fontStyle3,
                            command=self.button_pow)
        button_sqrt = Button(self.root, text="Sqrt", padx=20, pady=11, bg='#e6e9eb', bd=0, font=self.fontStyle3,
                             command=self.button_sqrt)
        button_back = Button(self.root, text="Back", padx=16, pady=12, bg='#e6e9eb', bd=0, font=self.fontStyle3,
                             command=self.button_back)
        # BUTTONS CORDINATES
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
        self.changeOnHover(button_1, "#8c929c", "white")
        self.changeOnHover(button_2, "#8c929c", "white")
        self.changeOnHover(button_3, "#8c929c", "white")
        self.changeOnHover(button_4, "#8c929c", "white")
        self.changeOnHover(button_5, "#8c929c", "white")
        self.changeOnHover(button_6, "#8c929c", "white")
        self.changeOnHover(button_7, "#8c929c", "white")
        self.changeOnHover(button_8, "#8c929c", "white")
        self.changeOnHover(button_9, "#8c929c", "white")
        self.changeOnHover(button_0, "#8c929c", "white")
        self.changeOnHover(button_point, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_plus_minus, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_add, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_equal, "#5285d9", "#9dbff5")
        self.changeOnHover(button_clear, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_subtract, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_multiply, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_devide, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_fraction, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_pow, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_sqrt, "#8c929c", "#e6e9eb")
        self.changeOnHover(button_back, "#8c929c", "#e6e9eb")
        self.root.bind('1', lambda event, parameter=1: self.press(parameter))
        self.root.bind('2', lambda event, parameter=2: self.two(parameter))
        self.root.bind('3', lambda event, parameter=2: self.three(parameter))
        self.root.bind('4', lambda event, parameter=2: self.four(parameter))
        self.root.bind('5', lambda event, parameter=2: self.five(parameter))
        self.root.bind('6', lambda event, parameter=2: self.six(parameter))
        self.root.bind('7', lambda event, parameter=2: self.seven(parameter))
        self.root.bind('8', lambda event, parameter=2: self.eight(parameter))
        self.root.bind('9', lambda event, parameter=2: self.nine(parameter))
        self.root.bind('0', lambda event, parameter=2: self.zero(parameter))
        self.root.bind('+', self.button_add)
        self.root.bind('-', self.button_subtract)
        self.root.bind('/', self.button_devide)
        self.root.bind('*', self.button_multiply)
        self.root.bind('.', self.button_point)
        self.root.bind('<Return>', self.button_equal)
        self.root.bind('<Delete>', self.button_clear)
        self.root.bind('<BackSpace>', self.button_back)
        # BUTTON COLOR HOVER
        # function to change properties of button on hover
        self.root.mainloop()


if __name__ == "__main__":
    st = Base()
    st.main()
