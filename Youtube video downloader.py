from tkinter import Tk, Label, Entry, Button, font
from pytube import YouTube

def download_video():
    try:
        YouTube(url_entry.get()).streams.get_highest_resolution().download(path_entry.get())
        status_lablel.config(text = "Video downloaded Successfully")
    except Exception as e:
        status_lablel.config(text = f"Error:{e}")

root = Tk()
root.title("YouTube Downloader")

root.configure(bg = "#F57D1F")

Label_font = font.Font(family="Arial",size=12)
 
Label(root,text = "Enter YouTube video URl : ", bg = '#F72798',font = Label_font).pack()
url_entry = Entry(root,width =50 ,bg = '#FFFFFF')
url_entry.pack()

Label(root,text="Output Path: ",bg = '#7F27FF',font=Label_font).pack()
path_entry = Entry(root,width=50,bg='#FFFFFF')
path_entry.pack()

button_font = font.Font(family="Arial",size=15,weight='bold')

Button(root,text ="Download Video",command=lambda:download_video(),bg='#4CAF50',fg = "white",font= button_font).pack()
status_lablel = Label(root,text="",bg = '#F57D1F',font=Label_font)
status_lablel.pack()

root.mainloop()
