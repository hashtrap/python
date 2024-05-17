import matplotlib
import numpy as np

def calculate_avg():
    with open("partA_output_data.txt", "r") as file:
        for i in range(23):
          data = file.readline()
          data = data.split(",")
          print(data)

calculate_avg()