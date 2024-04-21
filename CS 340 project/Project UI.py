'''
Author: Stavri Gkousi
Date: 2021-02-21
Copyright: 2024 all ownership to author,permission required
Description: A simple ui and ai project in python
'''


# import necesaray modules
from tkinter import *

#create the window to see
window=Tk() # create the window

# customizing the winodw we will work
window.geometry('500x500+400+150') # position window
window.title('F1 data statistics') # give the window a title
window.iconphoto(False,PhotoImage(file="F1.png")) # set a logo for the program
window.config(background="#232A2F")

window.mainloop() # keeps the window on screen