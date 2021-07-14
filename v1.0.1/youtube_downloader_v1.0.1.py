#!/usr/bin/env python3

from tkinter import filedialog
from tkinter import *
import pyautogui
from pytube import YouTube
from threading import Thread

global x
global x2

def insert():
    pyautogui.hotkey('ctrl', 'v')
    txt1.delete(0, 'end')

def browse_button():
    filename = filedialog.askdirectory()
    txt2.delete(0, 'end')
    txt2.insert(0, filename)
    
def download():
    x = txt1.get()
    x2 = txt2.get()
    try:
        youtube = YouTube(x)
        video = youtube.streams.filter(res="720p").first()
        # ~ size_video = round(video.filesize/10**6, 1)
        print('Кліп:', youtube.title, 'розміром', youtube.length, 'буде завантажено в /home/grey/Відео/clips')
        lb3.config(text = "Завантаження:   " + youtube.title)
        video.download(x2)
        lb3.config(text = "Відео: " + youtube.title + " --- успішно завантажено в " + x2 , fg='green')
        lb4.config(text = "Розмір скачаного відеофайла становить: " + str(round(video.filesize/10**6, 1)) + "MB")
        
        print('Кліп завантажено розмір')
        
    except Exception:
        lb3.config(text = "Збій завантаження файла", fg='red', font=("Times New Roman", 16))
        
def starter():
	Thread(target=download,args=()).start()

    


window = Tk()
window.title("Програма загрузки роликів з YouTube v1.0")
window.configure(background='bisque')
window.resizable(False, False)
lb1 = Label(window, text="Вставте скопійоване посилання на відео з Youtube:", font=("Times New Roman", 14), bg='bisque')
lb2 = Label(window, text="Виберіть директорію для збереження відео:", font=("Times New Roman", 14), bg='bisque')
lb3 = Label(window, font=("Times New Roman", 10), bg='bisque', wraplength=500)
lb4 = Label(window, font=("Times New Roman", 10), bg='bisque')

lb1.grid(column=0, row=0, padx=(10, 0))
lb2.grid(column=0, row=2, padx=(10, 0))
lb3.grid(column=0, row=5, padx=(10, 0), pady=(10, 10))
lb4.grid(column=0, row=6, padx=(10, 0), pady=(10, 10))

btn1 = Button(window, text="Завантажити", width=40, command=starter)
btn2 = Button(window, text="Вставити", command=insert)
btn3 = Button(window, text="Вибрати", command=browse_button)
btn1.grid(column=0, row=4, padx=(10, 10))
btn2.grid(column=2, row=1, padx=(10, 10))
btn3.grid(column=2, row=3, padx=(10, 10))

txt1 = Entry(window, width=70, bd=2)
txt2 = Entry(window, width=70, bd=2)
txt1.grid(column=0, row=1, padx=(10, 10))
txt2.grid(column=0, row=3, padx=(10, 10), pady=(0, 10))

window.mainloop()
