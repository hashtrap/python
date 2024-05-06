'''
Author: Stavri Gkousi
Date: 2021-02-21
Copyright: 2024 all ownership to author,permission required
Description: A simple ui and ai project in python
'''
import time
from Races import *

race=Races()
def window():
    print("==================================================================")
    print("F1 GRAND PRIX RACING DATA & STATISTICS FOR THE 2023 RACING SEASON")
    print("==================================================================")
    print("1. Read and display the F1 Grand Prix data for the 2023 racing season")
    print("2. Filter and sort race data based on a minimum threshold of laps")
    print("3. Calculate average lap time per race, save, retrieve, display")
    print("4. Sort and display the data based on user parameters")
    print("5. Calculate and graph total lap time per driver")
    print("6. Exit the program \n")
def opt1():

    race.Display()
def opt2():
    target=input("Enter the limit of laps\n")
    race.limit_lap(int(target))

def opt3():
    race.avg_lap()
def opt4():
    toSort=input("Enter the value to sort by\n")
    order=input("Type yes if you want to sort by ascending or descending\n")
    race.value_sort(toSort,order)

def opt5():
    pass

while True:
    window()
 # try:

    ask=int(input("\nChoose one of the options above\n"))
    if ask==1:
        opt1()
    elif ask == 2:
         opt2()
    elif ask==3:
         opt3()
    elif ask==4:
        opt4()
    elif ask==5:
        opt5()
    elif ask==6:
        print("Exiting program,Goodbye")
        break
    else:
        print("Invalid option")
        time.sleep(2)
  #except ValueError:
     # print("Only numbers are allowed")
    # time.sleep(2)



