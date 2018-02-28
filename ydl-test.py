from __future__ import unicode_literals
import youtube_dl
import os


def grab(link):
    path = (input("Where do you want to download it: "))
    
    if len(path) > 0:
        path =(input("Please select a directory: "))
    else:
        path = os.getcwd()
        
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{path}\%(title)s.%(ext)s',  #path will be defined on main.py
    #'simulate' : True,    #only here for testing
    'default_search' : 'auto',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return


url = input("Search for a song or enter a link: ")

while len(url) == 0:
    
    print ("No url entered")
    url = input("Please enter a URL")

grab(url)