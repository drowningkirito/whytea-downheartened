import tkinter as tk
import ttkbootstrap as ttk
import os
import requests as re
from pytube import YouTube
from tkinter import messagebox,filedialog
from PIL import Image,ImageTk
import requests as re
def on_callback(video_stream,total_size,bytes_remaining):
        total_size=video_stream.filesize
        bytes_downloaded=total_size-bytes_remaining
        percentage_completed=(bytes_downloaded/total_size)*100
        pbar["value"]+=int(percentage_completed)
        proglabel.config(text=str(percentage_completed))
        pbar.update_idletasks()
        if bytes_downloaded>=total_size:
            proglabel.config(text="Successfully Downloaded")

class Mydown():
    def chckmenu(self):
        # path=filedialog.askdirectory()
        # name=path.split("/")
        ressel=menu.get()
        stream=yt.streams.get_by_itag(dwn[ressel])
        # stream.download(output_path=path)
        stream.download()
    
    
    def __init__(self,window,url):
        self.window=window
        self.url=url
        self.window.geometry("1000x700+200+0")
        
        photoimage=tk.PhotoImage(file="downloader.png")
        self.window.iconphoto(False,photoimage)
        self.window.title("YtVidDownloader")
        global yt
        yt=YouTube(self.url,on_progress_callback=on_callback)        
        thumbnail = ImageTk.PhotoImage(Image.open(re.get(yt.thumbnail_url, stream=True).raw))

        tk.Label(self.window,image=thumbnail,width=700,height=400).pack(pady=5)
        b1=ttk.Label(self.window,text="Select Quality:",
                     bootstyle="inverse-light",
                     font=("Arial",15),
                    )
        b1.pack()
        video_itag=[]
        audio_itag=[]
        global dwn
        dwn=dict()
        # for i in yt.streams.filter(progressive=True).order_by("resolution"):
        #     video_itag.append(i.resolution)
        #     video_itag.append(i.itag)
        # for v in range(0,len(video_itag),2):
        #     dwn[video_itag[v]]=video_itag[v+1]
        for i in yt.streams.filter(progressive=True).order_by("resolution"):
            video_itag.append(i.resolution)
            video_itag.append(i.itag)
        for j in yt.streams.filter(adaptive=True).order_by("abr"):
            audio_itag.append(j.abr)
            audio_itag.append(j.itag)
        vid_aud=video_itag+audio_itag
        for v in range(0,len(vid_aud),2):
            dwn[vid_aud[v]]=vid_aud[v+1]        
        global menu
        menu=ttk.Combobox(self.window,text="Available Quality:",
                          bootstyle="info",
                          state="readonly",
                         values=tuple(dwn.keys()))
        menu.current(0)
        menu.pack(pady=20)
        global pbar
        pbar=ttk.Progressbar(window,bootstyle="danger-stripped",
                     length=300,
                     value=0,
                     maximum=100)
        pbar.pack(pady=0)
        global proglabel
        proglabel=ttk.Label(window,bootstyle="light",
                       font=("Arial", 15))
        proglabel.pack(pady=0)
    
        down=ttk.Button(self.window,text="Download",bootstyle="info-outline",command=self.chckmenu)
        down.pack(pady=60)
    

        self.window.mainloop()
    

if __name__=="__main__":
    url="https://www.youtube.com/watch?v=9M_ZKSmxb_s"
    window=ttk.Window(themename="solar")
    app=Mydown(window,url)