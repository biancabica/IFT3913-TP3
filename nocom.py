from scipy.stats import kstest
from scipy.stats import anderson
from scipy.stats import shapiro
import csv
import numpy
nocom = []

with open ("/Users/biancabica/Downloads/jfreechart-statsoriginal.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        nocom = numpy.append(nocom, float(row[1]))

    print(kstest(nocom, 'norm'))
    print(anderson(nocom, 'norm'))
    print(shapiro(nocom))








