import time
import math
from Sorter import *

class Races:

    def __init__(self):
        self.grand_prix = []
        self.date = []
        self.winner = []
        self.car = []
        self.laps = []
        self.time = []
        with open("partA_input_data.txt","r") as file:
            line=[]


            for i in range(23):
                field = []
                line.append(file.readline())
                field=line[i].split(',')
                self.grand_prix.append(field[0])
                self.date.append(field[1])
                self.winner.append(field[2])
                self.car.append(field[3])
                self.laps.append(field[4])
                self.time.append(field[5])
        self.grand_prix.pop(0)
        self.date.pop(0)
        self.winner.pop(0)
        self.car.pop(0)
        self.laps.pop(0)
        self.time.pop(0)






    def Display(self):
       for i in range(len(self.grand_prix)):
           print(self.grand_prix[i])
           print(self.date[i])
           print(self.winner[i])
           print(self.car[i])
           print(self.laps[i])
           print(self.time[i])
           time.sleep(0.5)

    def limit_lap(self,target):
        above_thresh=[]


        for i in range(0,len(self.grand_prix)):
            if int(target)<=int(self.laps[i]):
                above_thresh.append(self.grand_prix[i]+" "+self.date[i]+" "+self.winner[i]+" "+
                                   self.car[i]+" "+self.laps[i]+" "+self.time[i])
        above_thresh=sorted(above_thresh)
        for j in range(0,len(above_thresh)):
            print(above_thresh[j])

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

        for i in range(0,len(times)):
            avg.append(format((hours[i]*3600+minutes[i]*60+seconds[i])/int(self.laps[i]),".2f"))

        with open("partA_output_data.txt","w") as file:
               file.write("GRAND PRIX,DATE,WINNER,CAR,LAPS,TIME,AVERAGE_LAP\n")

               for i in range(0,len(self.grand_prix)):
                   hour=math.floor(round(float(avg[i]))/3600)
                   min=math.floor(round(float(avg[i])%3600)/60)
                   sec=math.floor((round(float(avg[i]))%3600)%60)
                   file.write(self.grand_prix[i]+","+self.date[i]+","+self.winner[i]
                              +","+self.car[i]+","+self.laps[i]+","
                              +self.time[i] +","+str(hour)+":"+str(min)+":"+str(sec)+"\n")

    def value_sort(self,category,order):
        sort=Sorter()
        if str(category).lower() == "winner":
            fixed=sort.BubbleSort(self.winner,order)
            i=0
            while i<len(self.winner):
                if self.winner[i]==fixed[i]:
                    print(self.grand_prix[i])
                    print(self.date[i])
                    print(self.winner[i])
                    print(self.car[i])
                    print(self.laps[i])
                    print(self.time[i])
                    i+=1
                else:
                    i+=1
        elif str(category).lower() == "grand prix":
          fixed = sort.BubbleSort(self.grand_prix,order)
          i = 0
          while i < len(self.grand_prix):
            if self.grand_prix[i] == fixed[i]:
                print(self.grand_prix[i])
                print(self.date[i])
                print(self.winner[i])
                print(self.car[i])
                print(self.laps[i])
                print(self.time[i])
                i += 1
            else:
                i += 1
        elif str(category).lower() == "date":
          fixed = sort.BubbleSort(self.date,order)
          i = 0
          while i < len(self.date):
            if self.date[i] == fixed[i]:
                print(self.grand_prix[i])
                print(self.date[i])
                print(self.winner[i])
                print(self.car[i])
                print(self.laps[i])
                print(self.time[i])
                i += 1
            else:
                i += 1
        elif str(category).lower() == "car":
          fixed = sort.BubbleSort(self.car,order)
          i = 0
          while i < len(self.car):
            if self.car[i] == fixed[i]:
                print(self.grand_prix[i])
                print(self.date[i])
                print(self.winner[i])
                print(self.car[i])
                print(self.laps[i])
                print(self.time[i])
                i += 1
            else:
                i += 1
        elif str(category).lower() == "laps":
          fixed = sort.BubbleSort(self.laps,order)
          i = 0
          while i < len(self.laps):
            if self.laps[i] == fixed[i]:
                print(self.grand_prix[i])
                print(self.date[i])
                print(self.winner[i])
                print(self.car[i])
                print(self.laps[i])
                print(self.time[i])
                i += 1
            else:
                i += 1
        elif str(category).lower() == "time":
          fixed = sort.BubbleSort(self.time,order)
          i = 0
          while i < len(self.time):
            if self.time[i] == fixed[i]:
                print(self.grand_prix[i])
                print(self.date[i])
                print(self.winner[i])
                print(self.car[i])
                print(self.laps[i])
                print(self.time[i])
                i += 1
            else:
                i += 1
race=Races()
race.value_sort("laps",False)