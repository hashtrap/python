import csv
import time
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

