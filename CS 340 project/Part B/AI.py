'''
Author: Stavri Gkousi
Date: 2022-02-21
Email: 20220338@student.act.edu
Copyright: Full Rights reserved for the author, source code found from authors personal repository
'''
import time

def opt1():
    pass


def opt2():
    pass


def opt3():
    pass


def opt4():
    pass


def opt5():
    pass


def window():
    print("==================================================================")
    print("USER MENU: MLP CLASSIFICATION OF THE ###### DATA SET (UCI REPOSITORY)")
    print("==================================================================")
    print("1. Read the labelled text data file, display the first 5 lines")
    print("2. Choose the size of the hidden layers of the MLP topology (e.g. 6-?-?-2)")
    print("3. Choose the size of the training step (0.001 - 0.5, [ENTER] for adaptable)")
    print("4. Train on 80% of labeled data, display progress graph")
    print("5. Classify the unlabeled data, output training report and confusion matrix")
    print("6. Exit the program \n")


while True:
        window()
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