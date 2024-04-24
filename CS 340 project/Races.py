import csv
import time
import math
class Races:

    def __init__(self):
        with open("partA_input_data.csv","r") as file:
            csvFile = csv.reader(file)
            self.grand_prix=[]
            self.date=[]
            self.winner=[]
            self.car=[]
            self.laps=[]
            self.time=[]
            for lines in csvFile:
                self.grand_prix.append(lines[0])
                self.date.append(lines[1])
                self.winner.append(lines[2])
                self.car.append(lines[3])
                self.laps.append(lines[4])
                self.time.append(lines[5])
        self.grand_prix.pop(0)
        self.date.pop(0)
        self.winner.pop(0)
        self.car.pop(0)
        self.laps.pop(0)
        self.time.pop(0)

    def Display(self):
        with open("partA_input_data.csv","r") as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)
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
        for i in range(len(self.time)):
            times.append(self.time[i].split(":"))
        avg=[]
        hours=[]
        minutes=[]
        seconds=[]


        for j in range(0, len(times)):
            hours.append(int(times[j][0]))
            minutes.append(int(times[j][1]))
            seconds.append(int(times[j][2]))

        for i in range(0,len(times)):
            avg.append(format((hours[i]*3600+minutes[i]*60+seconds[i])/int(self.laps[i]),".2f"))

        with open("hey.txt","w") as file:
               file.write("GRAND PRIX,DATE,WINNER,CAR,LAPS,TIME,AVERAGE_LAP\n")

               for i in range(0,len(self.grand_prix)):
                   hour=math.floor(round(float(avg[i]))/3600)
                   min=math.floor(round(float(avg[i])%3600)/60)
                   sec=math.floor((round(float(avg[i]))%3600)%60)
                   file.write(self.grand_prix[i]+","+self.date[i]+","+self.winner[i]+","+self.car[i]+","
                             +self.laps[i]+","+self.time[i]+","+str(hour)+":"+str(min)+":"+str(sec)+"\n")







