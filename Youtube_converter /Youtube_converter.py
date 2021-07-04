import youtube_dl
import tkinter

version = '1.1'             # this is version

window = tkinter.Tk()                   # creation window
window.geometry('600x400')              #
window.title('Youtube converter mp3')   #
window.resizable(width=0, height=0)     #

img = tkinter.PhotoImage(file='3.png')      # add background image
bg = tkinter.Label(window, image=img)       #
bg.place(x=0, y=0)                          #

box = tkinter.Entry()                   # creation text box
box.pack()                              #
box.place(x=220, y=180)                 #

version = tkinter.Label(window, text=f'v  {version}', bg='black')        # creation version label
version.pack(side='right', anchor='s')                                   #


def converter(url):                                   # function that request URL and convert and download the mp3 sound
    audiod = youtube_dl.YoutubeDL({'format': 'bestaudio', 'postprocessors': [{ 'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192', }]})

    try:
        audiod.extract_info(url)

        text_download = tkinter.Tk()                                        # creation download label window
        text_download.geometry('300x150')                                   #
        text_download.title('Download')                                     #

        tdl = tkinter.Label(master=text_download,
                            text='Video downloaded successfully', font=13)     # creation text download label
        tdl.pack()                                                             #
        tdl.place(x=20, y=50)                                                  #

    except:
        text_error = tkinter.Tk()                           # creation window that show label error
        text_error.geometry('200x100')                      #
        text_error.title('ERROR')                           #

        label_error = tkinter.Label(master=text_error, text='Invalid URL!', font=15, fg='red')    # creation label error
        label_error.pack()                                                                        #
        label_error.place(x=55, y=35)                                                             #


button = tkinter.Button(master=window, command=lambda: converter(box.get()))                       # creation button
button.config(text='Converti e scarica', fg='white', bg='black')                                   #
button.pack(padx=20)                                                                               #
button.place(x=230, y=202)                                                                         #

author = tkinter.Label(master=window, text='Created by  SV975', font=13, bg='black')  # creation author label
author.pack(side='left', anchor='s')                                                             #

window.mainloop()
