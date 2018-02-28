"""ignore for now. wrote all this on an online repl so I doubt it actually works
"""

import tkinter
from tkinter import ttk

root = tkinter.tk()

frame = Frame(root)
frame.pack()

#pic = Image.open(D:\python\images\)   #DL button image. will fill in
#URL/search entry field+ label
url_label = Label(top, text="Search or enter URL")
url_label.pack(side = left)
ent_url = Entry(top, bd=5)
ent_url.pack(side = right)

#directory entry field + label
path_label = Label(bottom, text="Directory")
path_label.pack(side = left)
path_ent = Entry(bottom, bd=5)
path_ent.pack(side = right)

#download button using entries from previous fields(hopefully)
download_but = Button(bottom, command= grab_link.grab(ent_url(get), path_ent(get)))
download_but.pack(side = bottom)



root.mainloop()

