import pandas as pd 
import plotly_express as plotly_express 
import csv
import numpy as np
 
def getdatasource(data_path):
    cups_of_coffee=[]
    sleeping_hours=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            sleeping_hours.append(float(row["sleep in hours"]))
    return{"x":cups_of_coffee,"y":sleeping_hours}
def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(correlation)
def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = getdatasource(data_path)
    find_correlation(data_source)
setup()