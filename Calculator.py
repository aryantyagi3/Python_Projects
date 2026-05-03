from tkinter import *
from PIL import Image, ImageTk

First_Number = Second_Number = Operator = None

# FUNCTIONs
def get_digit(Digit):
    current = result_label["text"]
    new = current + str(Digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(op):
    global First_Number, Operator
    First_Number = int(result_label["text"])
    Operator = op
    result_label.config(text="")

def get_result():
    global First_Number, Second_Number, Operator
    try:
        Second_Number = int(result_label["text"])

        if Operator == "+":
            result_label.config(text=str(First_Number + Second_Number))
        elif Operator == "-":
            result_label.config(text=str(First_Number - Second_Number))
        elif Operator == "*":
            result_label.config(text=str(First_Number * Second_Number))
        elif Operator == "/":
            if Second_Number == 0:
                result_label.config(text="ERROR!")
            else:
                result_label.config(text=str(round(First_Number / Second_Number)))
    except:
        result_label.config(text="ERROR!")

# GUI
window = Tk()
window.title("CALCULATOR")
window.geometry("360x350")
window.resizable(0, 0)
window.config(background="Black")

# ICON
icon_image = ImageTk.PhotoImage(Image.open("Calculator_Icon.png"))
window.iconphoto(False, icon_image)

# LABELs
result_label = Label(window, text= "", bg= "Black", fg= "White")
result_label.grid(row=0, column=0, columnspan=5, pady=(50, 25), sticky="w")
result_label.config(font=("ADLaM Display", 30, "bold"))

button_7 = Button(window, text= "7", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(7))
button_7.grid(row=1, column=0)
button_7.config(font=("Arial Rounded MT Bold", 10))

button_8 = Button(window, text= "8", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(8))
button_8.grid(row=1, column=1)
button_8.config(font=("Arial Rounded MT Bold", 10))

button_9 = Button(window, text= "9", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(9))
button_9.grid(row=1, column=2)
button_9.config(font=("Arial Rounded MT Bold", 10))

button_clear = Button(window, text= "AC", bg= "Grey", fg= "White", width=10, height=3, command=lambda : clear())
button_clear.grid(row=1, column=3)
button_clear.config(font=("Arial Rounded MT Bold", 10))

button_4 = Button(window, text= "4", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(4))
button_4.grid(row=2, column=0)
button_4.config(font=("Arial Rounded MT Bold", 10))

button_5 = Button(window, text= "5", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(5))
button_5.grid(row=2, column=1)
button_5.config(font=("Arial Rounded MT Bold", 10))

button_6 = Button(window, text="6", bg="Grey", fg="White", width=10, height=3, command=lambda : get_digit(6))
button_6.grid(row=2, column=2)
button_6.config(font=("Arial Rounded MT Bold", 10))

button_add = Button(window, text= "+", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_operator("+"))
button_add.grid(row=2, column=3)
button_add.config(font=("Arial Rounded MT Bold", 10))

button_1 = Button(window, text= "1", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(1))
button_1.grid(row=3, column=0)
button_1.config(font=("Arial Rounded MT Bold", 10))

button_2 = Button(window, text= "2", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(2))
button_2.grid(row=3, column=1)
button_2.config(font=("Arial Rounded MT Bold", 10))

button_3 = Button(window, text= "3", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(3))
button_3.grid(row=3, column=2)
button_3.config(font=("Arial Rounded MT Bold", 10))

button_minus = Button(window, text= "-", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_operator("-"))
button_minus.grid(row=3, column=3)
button_minus.config(font=("Arial Rounded MT Bold", 10))

button_divide = Button(window, text= "/", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_operator("/"))
button_divide.grid(row=4, column=0)
button_divide.config(font=("Arial Rounded MT Bold", 10))

button_0 = Button(window, text= "0", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_digit(0))
button_0.grid(row=4, column=1)
button_0.config(font=("Arial Rounded MT Bold", 10))

button_multiplication = Button(window, text= "*", bg= "Grey", fg= "White", width=10, height=3, command=lambda : get_operator("*"))
button_multiplication.grid(row=4, column=2)
button_multiplication.config(font=("Arial Rounded MT Bold", 10))

button_equal = Button(window, text= "=", bg= "Grey", fg= "White", width=10, height=3, command=get_result)
button_equal.grid(row=4, column=3)
button_equal.config(font=("Arial Rounded MT Bold", 10))

window.mainloop()