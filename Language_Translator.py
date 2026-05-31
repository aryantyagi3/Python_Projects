from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from googletrans import Translator, LANGUAGES 

# FUNCTIONs
def translate(text= "Type", org= "English", convert= "Hindi"):
    phrase = text
    source = org
    destination = convert
    change = Translator()
    content = change.translate(text, src= source, dest= destination)
    return content.text

def data():
    original = original_language.get()
    converted = converted_language.get()
    message = primary_text.get(1.0, END)
    word = translate(text= message, org= original, convert= converted)
    secondary_text.delete(1.0, END)
    secondary_text.insert(END, word)

# GUI
window = Tk()
window.title("LANGUAGE TRANSLATOR")
window.geometry("900x375")
window.config(bg= "Black")
window.resizable(0, 0)

# ICON
icon_image = ImageTk.PhotoImage(Image.open("LanguageTranslator_Icon.png"))
window.iconphoto(False, icon_image)

# IMAGE
swap = ImageTk.PhotoImage(Image.open("Swap.png"))
Label(window, image= swap, bg= "Black").place(x=370, y=95)

# LABELs
translator = Label(window, text= "TRANSLATOR", bg= "Black", fg= "White", font= ("ADLaM Display", 25, "bold"))
translator.place(x=332, y=17.5)

# FRAMEs
frame_1 = Frame(window).pack()
frame_2 = Frame(window).pack()

primary_text = Text(frame_1, bg= "White", fg= "Black", font= ("Arial Rounded MT Bold", 12), wrap= WORD)
primary_text.place(height= 270, width= 315, x=25, y=78)

secondary_text = Text(frame_2, bg= "White", fg= "Black", font= ("Arial Rounded MT Bold", 12), wrap= WORD)
secondary_text.place(height= 270, width= 315, x=555, y=78)

# LANGUAGEs
language = list(LANGUAGES.values())

original_language = ttk.Combobox(window, value= language)
original_language.place(x=25, y=47, height= 25, width= 175)
original_language.set("english")

converted_language = ttk.Combobox(window, value= language)
converted_language.place(x=695, y=47, height= 25, width= 175)
converted_language.set("english")

# BUTTONs
button = Button(window, text= "TRANSLATE", bg= "Black", fg= "White", border= 5, font= ("Arial Rounded MT Bold", 15, "bold"), command= data)
button.place(x=370, y=290)

window.mainloop()