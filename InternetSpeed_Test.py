from tkinter import *
from PIL import Image, ImageTk
import speedtest

# FUNCTIONs
def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()
    download = str(round(st.download()/(10**6), 0))
    upload = str(round(st.upload()/(10**6), 0))
    servernames = []
    st.get_servers(servernames)
    
    download_speed.config(text= download)
    download_speed1.config(text= download)
    upload_speed.config(text= upload)
    ping.config(text= st.results.ping)

# GUI
window = Tk()
window.title("INTERNET SPEED TESTER")
window.geometry("450x600")
window.config(bg= "#1a212d")
window.resizable(0, 0)

# ICON
icon_image = ImageTk.PhotoImage(Image.open("SpeedTest_Icon.png"))
window.iconphoto(False, icon_image)

# IMAGEs
ping_image = ImageTk.PhotoImage(Image.open("Ping.png"))
Label(window, image= ping_image, bg= "#1a212d").place(x=40, y=0)

speed_image = ImageTk.PhotoImage(Image.open("Speed.png"))
Label(window, image= speed_image, bg= "#1a212d").place(x=50, y=175)

start_image = ImageTk.PhotoImage(Image.open("Start.png"))
Label(window, image= start_image, bg= "#1a212d").place(x=115, y=520)

# LABELs
download_label = Label(window, text= "DOWNLOAD", font= ("ADLaM Display", 15, "bold"))
download_label.config(bg= "#1a212d", fg= "White")
download_label.place(x=275, y=135)

download_speed = Label(window, text= "00", font= ("ADLaM Display", 15, "bold"))
download_speed.config(bg= "#313F5C", fg= "White")
download_speed.place(x=310, y=53)

download_label1 = Label(window, text= "DOWNLOAD SPEED", font= ("ADLaM Display", 20, "bold"))
download_label1.config(bg= "#313F5C", fg= "White")
download_label1.place(x=83, y=450)

download_speed1 = Label(window, text= "00", font= ("ADLaM Display", 20, "bold"))
download_speed1.config(bg= "#313F5C", fg= "White")
download_speed1.place(x=195, y=300)

upload_label = Label(window, text= "UPLOAD", font= ("ADLaM Display", 15, "bold"))
upload_label.config(bg= "#1a212d", fg= "White")
upload_label.place(x=70, y=135)

upload_speed = Label(window, text= "00", font= ("ADLaM Display", 15, "bold"))
upload_speed.config(bg= "#313F5C", fg= "White")
upload_speed.place(x=90, y=53)

ping_label = Label(window, text= "PING", font= ("ADLaM Display", 15, "bold"))
ping_label.config(bg= "#1a212d", fg= "White")
ping_label.place(x=195, y=135)

ping = Label(window, text= "00", font= ("ADLaM Display", 15, "bold"))
ping.config(bg= "#313F5C", fg= "White")
ping.place(x=195, y=53)

mbps1 = Label(window, text= "/Mbps", font= ("ADLaM Display", 10, "bold"))
mbps1.config(bg= "#313F5C", fg= "White")
mbps1.place(x=92, y=95)

mbps2 = Label(window, text= "/Ms", font= ("ADLaM Display", 10, "bold"))
mbps2.config(bg= "#313F5C", fg= "White")
mbps2.place(x=210, y=95)

mbps3 = Label(window, text= "/Mbps", font= ("ADLaM Display", 10, "bold"))
mbps3.config(bg= "#313F5C", fg= "White")
mbps3.place(x=312, y=95)

mbps4 = Label(window, text= "/Mbps", font= ("ADLaM Display", 15, "bold"))
mbps4.config(bg= "#313F5C", fg= "White")
mbps4.place(x=190, y=330)

# BUTTONs
start_button = Button(window, text= "START", font= ("ADLaM Display", 20, "bold"), command= speedcheck) 
start_button.config(bg= "#222E43", fg= "White", bd=0)
start_button.place(x=170, y=533)

window.mainloop()