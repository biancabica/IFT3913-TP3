from scipy.stats import kstest
from scipy.stats import anderson
from scipy.stats import shapiro
import csv
import numpy
#import pandas as pd

ncloc = []

with open ("/Users/biancabica/Downloads/jfreechart-statsoriginal.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        ncloc = numpy.append(ncloc, float(row[2]))

    print(kstest(ncloc, 'norm'))
    print(anderson(ncloc, 'norm'))
    print(shapiro(ncloc))







