import time
import math
from Sorter import *

class Races:

# create constructor to load information
    def __init__(self):
        self.grand_prix = []
        self.date = []
        self.winner = []
        self.car = []
        self.laps = []
        self.time = []
        with open("partA_input_data.txt", "r") as file:
            line=[]

# Load the data int the objects lists
            for i in range(23):
                line.append(file.readline())
                field=line[i].split(',')
                self.grand_prix.append(field[0])
                self.date.append(field[1])
                self.winner.append(field[2])
                self.car.append(field[3])
                self.laps.append(field[4])
                self.time.append(field[5].replace('\n',''))
# removes the first element because it contains the name of the column
        self.grand_prix.pop(0)
        self.date.pop(0)
        self.winner.pop(0)
        self.car.pop(0)
        self.laps.pop(0)
        self.time.pop(0)





# Created a method for displaying what the original file has
    def Display(self):
       for i in range(len(self.grand_prix)):
           print(self.grand_prix[i])
           print(self.date[i])
           print(self.winner[i])
           print(self.car[i])
           print(self.laps[i])
           print(self.time[i])
           time.sleep(0.5) # Delays print for asthetic purposes

# Created a method that will display the inforamtion that has a number of laps
# above a given limit
    def limit_lap(self,target):
        above_thresh=[]


        for i in range(0,len(self.grand_prix)):
            if int(target)<=int(self.laps[i]):
                above_thresh.append(self.grand_prix[i]+" "+self.date[i]+" "+self.winner[i]+" "+
                                   self.car[i]+" "+self.laps[i]+" "+self.time[i])
        above_thresh=sorted(above_thresh)
        for j in range(0,len(above_thresh)):
            print(above_thresh[j],"\n")
            time.sleep(1)

# Created a method to write the new file with the added field
    def avg_lap(self):
        times = []
        avg = []
        hours = []
        minutes = []
        seconds = []

        for i in range(len(self.time)):
            times.append(self.time[i].split(":"))



        for j in range(0, len(times)):
            hours.append(int(times[j][0]))
            minutes.append(int(times[j][1]))
            seconds.append(int(times[j][2]))
        # Turns the time values in the original file into seconds
        for i in range(0,len(times)):
            avg.append(format((hours[i]*3600+minutes[i]*60+seconds[i])/int(self.laps[i]),".2f"))

        with open("partA_output_data.txt", "w") as file:
               file.write("GRAND PRIX,DATE,WINNER,CAR,LAPS,TIME,AVERAGE_LAP\n")
               # Conversion of seconds into hours,minutes and seconds
               for i in range(0,len(self.grand_prix)):
                   hour=str(math.floor(round(float(avg[i]))/3600))
                   min=str(math.floor(round(float(avg[i])%3600)/60))
                   sec=str(math.floor((round(float(avg[i]))%3600)%60))
                   file.write(self.grand_prix[i]+","+self.date[i]+","+self.winner[i]
                              +","+self.car[i]+","+self.laps[i]+","+self.time[i]
                              +","+hour+":"+min+":"+sec+"\n")

# Created a method to sort the information according to the wanted field
    def value_sort(self,category,order):
        sort=Sorter()
        if str(category).lower() == "winner":
            fixed = self.winner.copy() # A copy of the original list because the sorting method passes list as a reference
            sorted = sort.BubbleSort(fixed, order)

            for j in range(0, len(fixed)):
                for i in range(0, len(fixed)):
                    if self.winner[i] == fixed[j]:
                        print(self.grand_prix[i])
                        print(self.date[i])
                        print(self.winner[i])
                        print(self.car[i])
                        print(self.laps[i])
                        print(self.time[i], "\n")
                        time.sleep(0.5)

                    else:
                        continue
        elif str(category).lower() == "grand prix":
          fixed = self.grand_prix.copy() # A copy of the original list because the sorting method passes list as a reference
          sorted=sort.BubbleSort(fixed,order)

          for j in range(0,len(fixed)):
              for i in range(0,len(fixed)):
                 if self.grand_prix[i] == fixed[j]:
                    print(self.grand_prix[i])
                    print(self.date[i])
                    print(self.winner[i])
                    print(self.car[i])
                    print(self.laps[i])
                    print(self.time[i],"\n")
                    time.sleep(0.5)

                 else:
                    continue
        elif str(category).lower() == "date":
         # No action needed the original file is already ordered by date
         if order:

            i = 0
            while i < len(self.date):

                print(self.grand_prix[i])
                print(self.date[i])
                print(self.winner[i])
                print(self.car[i])
                print(self.laps[i])
                print(self.time[i],"\n")
                time.sleep(0.5)
                i += 1
         else:
             i = len(self.date)-1
             while i >0:
                 print(self.grand_prix[i])
                 print(self.date[i])
                 print(self.winner[i])
                 print(self.car[i])
                 print(self.laps[i])
                 print(self.time[i], "\n")
                 time.sleep(0.5)
                 i -= 1
        elif str(category).lower() == "car":
            fixed = self.car.copy() # A copy of the original list because the sorting method passes list as a reference
            sorted = sort.BubbleSort(fixed, order)

            for j in range(0, len(fixed)):
                for i in range(0, len(fixed)):
                    if self.car[i] == fixed[j]:
                        print(self.grand_prix[i])
                        print(self.date[i])
                        print(self.winner[i])
                        print(self.car[i])
                        print(self.laps[i])
                        print(self.time[i], "\n")
                        time.sleep(0.5)

                    else:
                        continue
        elif str(category).lower() == "laps":
            fixed = self.laps.copy() # A copy of the original list because the sorting method passes list as a reference
            sorted = sort.BubbleSort(fixed, order)

            for j in range(0, len(fixed)):
                for i in range(0, len(fixed)):
                    if self.laps[i] == fixed[j]:
                        print(self.grand_prix[i])
                        print(self.date[i])
                        print(self.winner[i])
                        print(self.car[i])
                        print(self.laps[i])
                        print(self.time[i], "\n")
                        time.sleep(0.5)

                    else:
                        continue
        elif str(category).lower() == "time":
            fixed = self.time.copy() # A copy of the original list because the sorting method passes list as a reference
            sorted = sort.BubbleSort(fixed, order)

            for j in range(0, len(fixed)):
                for i in range(0, len(fixed)):
                    if self.time[i] == fixed[j]:
                        print(self.grand_prix[i])
                        print(self.date[i])
                        print(self.winner[i])
                        print(self.car[i])
                        print(self.laps[i])
                        print(self.time[i], "\n")
                        time.sleep(0.5)

                    else:
                        continue
        else:
            print("The option you have given isn't an option, Excecute abort")
            time.sleep(3)


