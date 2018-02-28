"""
2/25/18 youtube-dl project by REV

Using youtube-dl to download specified url or to search youtube and download first result. grab_link.py is the main function to this. This file is purely just prompts to download what you want and where you want it.

Also if I can get the GUI to work this file essentially becomes useless. 
"""


from __future__ import unicode_literals
import youtube_dl
import grab_link


url = input("Search for a song or enter a link:")

while len(url) == 0:
	
	print ("No url entered")
	url = input("Please enter a URL")
	
else:
	direct = input("Where would you like to download it?")
	while len(direct) == 0:
		print("No directory chosen,")
		direct = input("Please pick a directory")
		
	else:
		print("Ok, downloading file to" + " " + f"{direct}")
		grab_link.grab(url, direct)




