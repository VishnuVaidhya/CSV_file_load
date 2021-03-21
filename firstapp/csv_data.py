import csv
#from . models import Date_Store

with open('C:/Users/HP/Desktop/CSV/out1 django.csv') as csv_file:
    wrt = csv.writer(csv_file)
    cv = csv.reader(csv_file, delimiter=',')
    all_value = []
    for row in cv:
        data = row[2]
        print(data)
        #date_data = Date_Store(date=data)
        #date_data.save()


