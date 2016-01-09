import numpy
import pandas as pd

reader = pd.read_csv("numbers.csv", sep=',', engine='c', nrows = 20)
#reader2 = float(reader)
#print"1 reader=", reader
#print"2 reader=", reader
output = reader['Return']

print "output=",output

y = numpy.std(output)
print y
