from matplotlib import pyplot as plt
from Sorter import *
class Gui:
    def __calc_lap(self):
        with open("partA_output_data.txt", "r") as file:

            matrix = []
            for i in range(23):
                data = file.readline()
                matrix.append(data.split(","))

        winner = []
        laps = []
        for i in range(1, 23):
            winner.append(matrix[i][2])
            laps.append(matrix[i][6].replace("\n",""))

        driver = set(winner)
        driver = list(driver)

        times = [0]*len(driver)
        for i in range(len(driver)):
            for j in range(len(winner)):
                if driver[i] == winner[j]:
                    hour,minute,seconds=laps[j].split(":")
                    seconds=int(seconds)+(int(minute)*60)
                    times[i]=times[i]+seconds
                else:
                    pass
        avg_lap=[]
        for i in range(len(times)):
            hours, remainder = divmod(times[i], 3600)
            minutes, seconds = divmod(remainder, 60)
            avg_lap.append(str(hours)+":"+str(minutes)+":"+str(seconds))


        sort = Sorter()
        avg_lap = sort.BubbleSort(avg_lap, False)
        return avg_lap,driver


    def calc_lap(self):
       avg_lap,driver= self.__calc_lap()
       return avg_lap,driver

def calculate_avg():
    gui=Gui()
    avg_lap,driver=gui.calc_lap()

    plt.bar(driver,avg_lap,color="red",label=" Laps per minute")
    plt.xlabel('Drivers', fontsize=12)
    plt.ylabel('Laps per driver', fontsize=12)
    plt.title('Average laps per driver in all races', fontsize=20)
    plt.legend()
    plt.show()



