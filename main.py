from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import webbrowser
import numpy as np
import pickle


def contract_start():
    url = "https://www.facebook.com/profile.php?id=100003360365929&ref=bookmarks"
    webbrowser.open(url)


def start_button():

    return 0

window = Tk()
window.title("Real time screen translation")
window.geometry("400x400")
window.maxsize(width=400, height=400)
intro = Label(text="โปรแกรมแปลภาษาหน้าจอ")
intro.pack(pady=5)
bt = Button(window, text="เริ่ม", command=start_button)
bt.pack(pady=5)
contract = Label(text="จัดทำโดย ธีรพล อยู่คง")
contract.pack(pady=5)
bt2 = Button(window, text="ติดต่อ", command=contract_start)
bt2.pack(pady=5)
load = Image.open("abc.jpg")
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.image = render
img.place(x=100, y=150, height=200, width=200)
window.mainloop()
