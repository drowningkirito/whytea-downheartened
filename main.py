import tkinter as tk
import ttkbootstrap as ttk
import requests as re
from tkinter import messagebox
from pytube import YouTube
from dwncont import Mydown
import os

window= ttk.Window(themename="solar")
window.geometry("600x400+400+200")
photoimage = tk.PhotoImage(file="downloader.png")
window.iconphoto(False, photoimage)
window.title("YtVidDownloader")
global url

def validate_next():
    url_get = url.get()
    try:
        req = re.get(url_get)
        if req.status_code == 200:
            child = tk.Toplevel(window)
            nxtwin = Mydown(child, url_get)
             
            
            
    except:
        messagebox.showerror(title="Try Again", message="Can't Process Your Request Url, Check Url and Try Again!")
        


b1 = ttk.Label(window,text="Enter Link Below:",
                       bootstyle="inverse-light",
                       font=("Arial", 15),
                       )
b1.pack()

url = ttk.Entry(window,bootstyle="danger", width=65)
url.pack(pady=30)
submit = ttk.Button(window,text="Next", bootstyle="info-outline", width=20, command=validate_next)
submit.pack(pady=110)

window.mainloop()