from tkinter import *
from math import*

window = Tk()
#set expression
expression = ''

#button functions


def num_press(number):
    global expression
    expression += str(number)
    equation.set(expression)


def back_press():
    global expression
    equation.set(expression[:-1])
    expression = expression[:-1]

def equal_press():
    try:
        global expression
        answer = str(eval(expression))
        equation.set(answer)
        expression = answer

    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ''
    equation.set('')


window.geometry("240x320")
window.title("Scientific Calculator")
window.configure(background="#BFBEC0")
window.resizable(height=0, width=0)


equation = StringVar()
number_entry = Entry(window, textvariable=equation,  bg="#EAE3E3")
number_entry.grid(columnspan=6, row=0, ipadx=50, ipady=10, padx=10)



if __name__ == "__main__":
    b7 = Button(window, text="7", width=4, height=4, command=lambda: num_press(7), bg="#D9C8C0")
    b7.grid(row=1, column=0)

    b8 = Button(window, text="8", width=4, height=4, command=lambda: num_press(8), bg="#D9C8C0")
    b8.grid(row=1, column=1)

    b9 = Button(window, text="9", width=4, height=4, comman=lambda: num_press(9), bg="#D9C8C0")
    b9.grid(row=1, column=2)

    b4 = Button(window, text="4", width=4, height=4, command=lambda: num_press(4), bg="#D9C8C0")
    b4.grid(row=2, column=0)

    b5 = Button(window, text="5", width=4, height=4,command=lambda: num_press(5), bg="#D9C8C0")
    b5.grid(row=2, column=1)

    b6 = Button(window, text="6", width=4, height=4, command=lambda: num_press(6), bg="#D9C8C0")
    b6.grid(row=2, column=2)

    b1 = Button(window, text="1", width=4, height=4, command=lambda: num_press(1), bg="#D9C8C0")
    b1.grid(row=3, column=0)

    b2 = Button(window, text="2", width=4, height=4,command=lambda: num_press(2), bg="#D9C8C0")
    b2.grid(row=3, column=1)

    b3 = Button(window, text="3", width=4, height=4, command=lambda: num_press(3), bg="#D9C8C0")
    b3.grid(row=3, column=2)

    b0 = Button(window, text="0", width=4, height=4, command=lambda: num_press(0), bg="#D9C8C0")
    b0.grid(row=4, column=0)

    decimal = Button(window, text=".", width=4, height=4, command=lambda: num_press("."), bg="#D9C8C0")
    decimal.grid(row=4, column=1)

    equals = Button(window, text="=", width=4, height=4, command=lambda: equal_press(), bg="#F56A4E")
    equals.grid(row=4, column=2)

    add = Button(window, text="+", width=4, height=4, command=lambda: num_press("+"), bg="#F56A4E")
    add.grid(row=1, column=3)

    subtract = Button(window, text="-", width=4, height=4, command=lambda: num_press("-"), bg="#F56A4E")
    subtract.grid(row=2, column=3)

    multiply = Button(window, text="x", width=4, height=4, command=lambda: num_press("*"), bg="#F56A4E")
    multiply.grid(row=3, column=3)

    divide = Button(window, text="/", width=4, height=4, command=lambda: num_press("/"), bg="#F56A4E")
    divide.grid(row=4, column=3)

    exponent = Button(window, text="^", width=4, height=4, command=lambda: num_press("**"), bg="#D9C8C0")
    exponent.grid(row=2, column=5)

    right_para = Button(window, text=")", width=4, height=4, command=lambda: num_press(")"), bg="#D9C8C0")
    right_para.grid(row=1, column=5)

    left_para = Button(window, text="(", width=4, height=4, command=lambda: num_press("("), bg="#D9C8C0")
    left_para.grid(row=1, column=4)

    sin_func = Button(window, text="sin(", width=4, height=4, command=lambda: num_press("sin("), bg="#DAD8D9")
    sin_func.grid(row=2, column=4)

    cos_func = Button(window, text="cos(", width=4, height=4, command=lambda: num_press("cos("), bg="#DAD8D9")
    cos_func.grid(row=3, column=4)

    tan_func = Button(window, text="tan(", width=4, height=4, command=lambda: num_press("tan("), bg="#DAD8D9")
    tan_func.grid(row=4, column=4)

    clear = Button(window, text="clear", width=4, height=4, command=clear, bg="#696969")
    clear.grid(row=4, column=5)

    back = Button(window, text="back", width=4, height=4, command=lambda: back_press(), bg="#696969")
    back.grid(row=3, column=5)



    window.mainloop()
