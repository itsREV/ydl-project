
from __future__ import unicode_literals
import youtube_dl


def grab(link, path):
	#function to essentially call youtube_dl and to pass it the link and url entered
	path = {}
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