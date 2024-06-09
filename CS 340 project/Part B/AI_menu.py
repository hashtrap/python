'''
Author: Stavri Gkousi
Date: 2022-02-21
Email: 20220338@student.act.edu
Copyright: Full Rights reserved for the author, source code found from authors personal repository
'''
import time
from AI import *

# Create necessary object
Ai=Ai()

# Make the functions necessary for the work
def opt1():
    Ai.Display()


def opt2():
    Ai.Topology()


def opt3():
    Ai.Training_steps()



def opt4():
    Ai.Test_split()
    Ai.Training()


def opt5():
    Ai.Classification()
    Ai.Graphs()
    Ai.graph_18()

# Window to select options
def window():
    print("==================================================================")
    print("USER MENU: MLP CLASSIFICATION OF THE  BANK NOTE IDENTIFICATION DATA SET (UCI REPOSITORY)")
    print("==================================================================")
    print("1. Read the labelled text data file, display the first 5 lines")
    print("2. MLP topology")
    print("3. Training step")
    print("4. Train on 80% or 50-50")
    print("5. Classify data")
    print("6. Exit the program \n")


# Loop that runs forever until we tell it to stop
while True:
        window()
        # Statements that detect if we have not put a number as an option
        try:

            ask = int(input("\nChoose one of the options above\n"))
            if ask == 1:
                opt1()
            elif ask == 2:
                opt2()
            elif ask == 3:
                opt3()
            elif ask == 4:
                opt4()
            elif ask == 5:
                opt5()
            elif ask == 6:
                print("Exiting program,Goodbye")
                break
            else:
                print("Invalid option")
                time.sleep(2)
        except ValueError:
            print("Only numbers are allowed")
            time.sleep(2)