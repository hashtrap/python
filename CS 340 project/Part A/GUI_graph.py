from matplotlib import pyplot as py_lt

# Class to make the necessary object
class Gui:
    #Private method to do the file manipulation for security reasons
    def __calc_lap(self):
        with open("partA_output_data.txt", "r") as file:

            matrix = []
            for i in range(23):
                data = file.readline()
                matrix.append(data.split(","))

        winner = []
        laps = []
        races=[]
        for i in range(1, 23):
            winner.append(matrix[i][2])
            laps.append(matrix[i][6].replace("\n",""))
            races.append(matrix[i][0])

        driver = set(winner)
        driver = list(driver)
        times = [0]*len(driver)
        races_driver = [0]*len(driver)
        for i in range(len(driver)):
            for j in range(len(winner)):
                if driver[i] == winner[j]:
                    hour,minute,seconds=laps[j].split(":")
                    seconds=int(seconds)+(int(minute)*60)
                    times[i]=times[i]+seconds
                    races_driver[i]=int(races_driver[i]+1)
                else:
                    pass

        avg_lap=[]
        for i in range(len(times)):
            times[i]=int(round(int(times[i])/int(races_driver[i]),0))
            hours, remainder = divmod(times[i], 3600)
            minutes, seconds = divmod(remainder, 60)
            avg_lap.append(str(hours)+":"+str(minutes)+":"+str(seconds))



        return avg_lap,driver,races_driver

# A sort of getter method for the private method
    def calc_lap(self):
       avg_lap,driver,races_driver= self.__calc_lap()
       return avg_lap,driver,races_driver

# Method for creating the bar plot
def calculate_avg():
    gui=Gui()
    avg_lap=[]
    avg_lap,driver,races=gui.calc_lap()



    py_lt.bar(driver, avg_lap, color="red", label=" Laps per minute")
    py_lt.xlabel('Drivers', fontsize=12)
    py_lt.ylabel('Laps per driver', fontsize=12)
    py_lt.title('Average laps per driver in all races', fontsize=20)
    py_lt.legend()
    py_lt.show()



