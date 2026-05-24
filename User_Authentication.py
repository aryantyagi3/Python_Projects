from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# GUI
window = Tk()
window.title("USER AUTHENTICATION")
window.geometry("950x500")
window.config(bg= "White")
window.resizable(0, 0)

# SWITCH FRAMEs
def show_signup():
    signin_frame.place_forget()
    signup_frame.place(x=550, y=55)

def show_signin():
    signup_frame.place_forget()
    signin_frame.place(x=550, y=55)

# SIGN UP
def sign_up():
    username = signup_user.get()
    password = signup_code.get()
    confirm = signup_recode.get()

    if username == "" or password == "" or confirm == "":
        messagebox.showerror("ERROR", "All fields are required!")

    elif password != confirm:
        messagebox.showerror("ERROR", "Both Passwords should match!")

    else:
        file = open("User Info.txt", "a")
        file.write(username + ", " + password + "\n")
        file.close()

        messagebox.showinfo("SIGNED UP", "Account Created Successfully!")
        show_signin()

# FRAME
signup_frame = Frame(window, width= 350, height= 375, bg= "White")
Label(signup_frame, text= "Sign Up", bg= "White", fg= "Black", font= ("Arial", 30, "bold")).place(x=100, y=5)

# USERNAME
signup_user = Entry(signup_frame, width=25, border= 0, font= ("Arial", 11))
signup_user.place(x=40, y=105)

Frame(signup_frame, width= 275, height= 2, bg= "Black").place(x=40, y=130)

# PASSWORD
signup_code = Entry(signup_frame, width= 25, border= 0, font= ("Arial", 11), show= "*")
signup_code.place(x=40, y=165)

Frame(signup_frame, width= 275, height= 2, bg= "Black").place(x=40, y=190)

# CONFIRM PASSWORD
signup_recode = Entry(signup_frame, width= 25, border= 0, font= ("Arial", 11), show= "*")
signup_recode.place(x=40, y=225)

Frame(signup_frame, width= 275, height= 2, bg= "Black").place(x=40, y=250)

# BUTTONs
Button(signup_frame, text= "Sign Up", width= 32, bg= "Blue", fg= "White", command= sign_up).place(x=62, y=300)
Label(signup_frame, text= "Already have an account?", bg= "White").place(x=85, y=330)

Button(signup_frame, text= "Sign In", bg= "White", fg= "Blue", border= 0, cursor= "hand2", command= show_signin).place(x=225, y=330)

# SIGN IN
def sign_in():
    username = signin_user.get()
    password = signin_code.get()

    try:
        file = open("User Info.txt", "r")
        data = file.readlines()
        file.close()

        success = False

        for line in data:
            u, p = line.strip().split(",")

            if username == u and password == p:
                success = True
                break

        if success:
            screen = Toplevel(window)
            screen.title("WELCOME")
            screen.geometry("400x200")
            screen.config(bg= "White")

            Label(screen, text="You Are Successfully Signed In!", bg= "White", fg= "Black", font= ("Arial", 15, "bold")).pack(expand=True)

        else:
            messagebox.showerror("ERROR", "Invalid Username or Password!")

    except FileNotFoundError:
        messagebox.showerror("ERROR", "No Registered Users Found!")

# IMAGE
signin_image = ImageTk.PhotoImage(Image.open("SignIn.png"))
Label(window, image= signin_image, bg= "White").place(x=0, y=45)

# FRAME
signin_frame = Frame(window, width= 350, height= 375, bg= "White")
Label(signin_frame, text= "Sign In", bg= "White", fg= "Black", font= ("Arial", 30, "bold")).place(x=100, y=5)

# USERNAME
signin_user = Entry(signin_frame, width= 25, font= ("Arial", 11), border=0)
signin_user.place(x=45, y=130)

Frame(signin_frame, width= 260, height= 2, bg= "Black").place(x=45, y=150)

# PASSWORD
signin_code = Entry(signin_frame, width= 25, font= ("Arial", 11), border=0, show= "*")
signin_code.place(x=45, y=190)

Frame(signin_frame, width= 260, height= 2, bg= "Black").place(x=45, y=210)

# BUTTONs
Button(signin_frame, text= "Sign In", bg= "Blue", fg= "White", width= 32, command= sign_in).place(x=55, y=295)
Label(signin_frame,text= "Don't have an account?", bg= "White").place(x=85, y=325)

Button(signin_frame,text= "Sign Up", bg= "White", fg= "Blue", border= 0, cursor= "hand2", command= show_signup).place(x=215, y=325)

# PLACEHOLDER
def add_placeholder(entry, placeholder, is_password=False):

    entry.insert(0, placeholder)
    entry.config(fg= "Black")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, END)

            if is_password:
                entry.config(show= "*")

            entry.config(fg= "Black")

    def on_focus_out(event):
        if entry.get() == "":

            entry.insert(0, placeholder)

            if is_password:
                entry.config(show= "")

            entry.config(fg= "Black")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# (SIGN UP)
signup_user = Entry(signup_frame, width=25, border= 0, font= ("Arial", 11))
signup_user.place(x=52, y=105)
add_placeholder(signup_user, "Username")

signup_code = Entry(signup_frame, width= 25, border= 0, font= ("Arial", 11))
signup_code.place(x=52, y=165)
add_placeholder(signup_code, "Password", True)

signup_recode = Entry(signup_frame, width= 25, border= 0, font= ("Arial", 11))
signup_recode.place(x=52, y=225)
add_placeholder(signup_recode, "Confirm Password", True)

# (SIGN IN)
signin_user = Entry(signin_frame, width= 25, border= 0, font= ("Arial", 11))
signin_user.place(x=45, y=130)
add_placeholder(signin_user, "Username")

signin_code = Entry(signin_frame, width= 25, border= 0, font= ("Arial", 11))
signin_code.place(x=45, y=190)
add_placeholder(signin_code, "Password", True)

# START
show_signin()

window.mainloop()