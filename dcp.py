from scipy.stats import kstest
from scipy.stats import anderson
from scipy.stats import shapiro
import numpy
import csv

dcp = []

with open ("/Users/biancabica/Downloads/jfreechart-statsoriginal.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        dcp = numpy.append(dcp, float(row[3]))

    print(kstest(dcp,'norm'))
    print(anderson(dcp, 'norm'))
    print(shapiro(dcp))







