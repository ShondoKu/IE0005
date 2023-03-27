import csv
header_columns = []
csvfile = open('cardio_train.csv').readlines()
columns = csvfile[0].split(';')
columns[-1] = 'cardio'
header_columns = columns
print(header_columns)


