from matplotlib import pyplot as plt
from Sorter import *

def calculate_avg():
    with open("partA_output_data.txt", "r") as file:

        matrix=[]
        for i in range(23):
          data = file.readline()
          data
          matrix.append(data.split(","))


    winner=[]
    laps=[]
    for i in range(1,23):

        winner.append(matrix[i][2])
        laps.append(matrix[i][6])
    #winner = list(set(winner))
    print(winner)
    sort=Sorter()
    laps=sort.BubbleSort(laps,False)

    plt.bar(winner,laps,color="red",label=" Laps per minute")
    plt.xlabel('Drivers', fontsize=12)
    plt.ylabel('Laps per minute', fontsize=12)
    plt.title('Average laps per driver', fontsize=20)
    plt.legend()
    plt.show()



calculate_avg()