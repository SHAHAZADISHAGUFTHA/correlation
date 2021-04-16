import pandas as pd
import plotly_express as px 
import numpy as np
import csv

def getdatasource(data_path):
    Marks_Percentage = []
    Days_Present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    return{"x":Marks_Percentage,"y":Days_Present}
def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(correlation)
def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = getdatasource(data_path)
    find_correlation(data_source)
setup()