import tkinter as tk
from PIL import Image, ImageTk
import random

def Dice_Roll():
    Image_1 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    Label_1.config(image=Image_1)
    Label_1.image = Image_1

    Image_2 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    Label_2.config(image=Image_2)
    Label_2.image = Image_2

window = tk.Tk()
window.geometry("550x450")
window.title("DICE ROLL")
window.config(bg= "Black")

Dice = ["Dice 1.png", "Dice 2.png", "Dice 3.png", "Dice 4.png", "Dice 5.png", "Dice 6.png"]
Image_1 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
Image_2 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))

Label_1 = tk.Label(window, image=Image_1)
Label_2 = tk.Label(window, image=Image_2)

Label_1.Image = Image_1
Label_2.Image = Image_2

Label_1.place(x=55, y=115)
Label_2.place(x=365, y=115)

button = tk.Button(window, text="ROLL!!", bg= "White", fg= "Black", command=Dice_Roll)
button.config(font= ("ADLaM Display", 18, "bold"))
button.place(x= 225, y= 325)

window.mainloop()