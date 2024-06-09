'''
Author: Stavri Gkousi
Date: 2021-02-21
Copyright: 2024 all ownership to author,permission required
Description: A simple ui and ai project in python
'''
import time
from Races import *
import GUI_graph as gui
import os

# Creates the Object neccesary for operation
race=Races()
# Creates a window to display the possible options
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
    while True:

      try:
        target=int(input("Enter the limit of laps\n"))
        if target>0:
           race.limit_lap(int(target))
           break
        else:
           print("You must enter an integer greater than 0 \n")
           time.sleep(2)
      except ValueError:
        print("Error: Only numbers are allowed \n")
        time.sleep(2)

def opt3():
    race.avg_lap()
def opt4():

  if os.path.exists("partA_output_data.txt"):
    toSort=input("Enter the value to sort by [winner,grand prix,date,car,laps,time]\n")
    order=input("Type 0 or 1 if you want to sort by ascending or descending\n")
    if order=='1':
        race.value_sort(toSort,True)
    elif order=='0':
        race.value_sort(toSort,False)
    else:
        print("Value put is not an option so order will be ascending \n")
        time.sleep(3)
        race.value_sort(toSort, True)
  else:
     print("File does not exist,run option 3 first")
     time.sleep(3)

def opt5():
    gui.calculate_avg()

# Start an infinite loop that closes if user presses option 6
while True:
  window()
  # Check if we didn't put a number when asked
  try:

    ask=int(input("\nChoose one of the options above\n"))
    # If statements to check which option the user chose or if the option
    # he chose doesn't exist
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
  except ValueError:
      print("Only numbers are allowed")
      time.sleep(2)



