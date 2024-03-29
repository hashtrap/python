from tkinter import *
from tkinter import messagebox as msb
import random as rand
import os


def high_score():
    with open("High_score.txt") as file:
        checker = file.read()
        print(checker)
        window.title("High Score")
        intro.destroy()
        start_button.destroy()
        highscore_button.destroy()
        score = Label(window, text="High Score", bg="#B3E4FF", font=("ADLaM Display", 28), foreground="white")
        score.place(relx=0.5, rely=0.15,
                    anchor='center')
        high_score_list=Text(window, height=30, width=60,bg="white")
        high_score_list.insert(END, checker )
        high_score_list.place(relx=0.5, rely=0.6,
                    anchor='center')


        window.update()


# Window design
window = Tk()
window.title("Snake")
window.geometry("700x600+400+100")  # set the dimensions and the position of the window
window.configure(bg="#B3E4FF")  # design features of the window
photo = PhotoImage(file="snake.png")
window.iconphoto(TRUE, photo)

# Window elements Label
intro = Label(window, text="Welcome to Snake", bg="#B3E4FF", font=("ADLaM Display", 28), foreground="white")
intro.place(relx=0.5, rely=0.15,
            anchor='center')  # put the label in the desired postion and anchor it so no changes when maximising

# Window elements Button
start_button = Button(window, text="Start", bg="#FFDEB3"  # give text and background color to button
                      , activebackground="#FFDEB3", foreground="white"
                      # give text color and make backcolor not change when pressed
                      , activeforeground="white"
                      , font=("ADLaM Display", 16))  # make text color not change when pressed
start_button.place(relx=0.5, rely=0.45, anchor='center', width=200, height=40)  # give button position

highscore_button = Button(window, text="High Score", bg="#FFDEB3"  # give text and background color to button
                          , activebackground="#FFDEB3", foreground="white"
                          # give text color and make backcolor not change when pressed
                          , activeforeground="white"
                          , font=("ADLaM Display", 16)
                          , command=high_score)  # make text color not change when pressed
highscore_button.place(relx=0.5, rely=0.65, anchor='center', width=200, height=40)

window.mainloop()  # needed to keep the window showing until we exit

# Button functions
